import argparse
import torch
from classes.text_2_anime import TextToAnime
from classes.sketch_2_anime import SketchToAnime
from functions.load_lora_model import setup_text2img_with_lora, setup_img2img_with_lora
from app.config import Config

if __name__ == "__main__":
    print("🚀 Iniciando test.py ...")
    
    
    parser = argparse.ArgumentParser(description="Generar imágenes de anime a partir de texto o bocetos.")
    parser.add_argument("--input", type=str, required=False, help="Ruta de la imagen de entrada o texto.")
    parser.add_argument("--prompt", type=str, required=False, help="Texto descriptivo para la generación de imágenes.")
    parser.add_argument("--mode", type=str, choices=["text", "sketch"], required=True, help="Modo de operación: 'text' o 'sketch'.")
    args = parser.parse_args()

    random_name = "output_" + str(torch.randint(0, 10000, (1,)).item()) + ".png"
    if args.mode == "text" and args.input is None:
        
        pipe = setup_text2img_with_lora(Config.MODEL_ID, r"D:\Ciencias\Drawnime\ai_models\sketch_to_anime_lora_final")
        text_to_anime = TextToAnime(pipe)

        # prompt = input("Inserte el boceto y presiona Enter...")
        prompt = args.prompt if args.prompt else "anime style, high quality, detailed"
        
        result = text_to_anime.generate(prompt=prompt, num_inference_steps=5)
        result.save(f"results/{random_name}")

    elif args.mode == "sketch":
        prompt = args.prompt if args.prompt else "anime style, high quality, detailed"
        pipe = setup_img2img_with_lora(Config.MODEL_ID, r"D:\Ciencias\Drawnime\ai_models\sketch_to_anime_lora_final")
        sketch_to_anime = SketchToAnime(pipe)

        result = sketch_to_anime.generate(args.input, prompt=prompt)
        result.save(f"results/{random_name}")
