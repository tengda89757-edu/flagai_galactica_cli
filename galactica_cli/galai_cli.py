from flagai.model.predictor.predictor import Predictor
from flagai.auto_model.auto_loader import AutoLoader
import torch
import argparse
import json
import sys
import os


def process_args():
    parser = argparse.ArgumentParser(prog='GALACTICA cli',
                                     description='CLI interface for GALACTICA',
                                     epilog='See https://github.com/paperswithcode/galai and galactica.org '
                                            'for more information on the GALACTICA model.')
    parser.add_argument(
        'prompt', type=str,
        help='Prompt for the language model. \n'
             'Special tokens are used to nudge the language model to perform specific tasks, they include: \n'
             '[START_REF] : insert a Reference. \n'
             '<work> : reason about a question posed in the prompt. \n' 
             'TLDR: : produce a TLDR summary of the prompt. \n'
             '[START_I_SMILES] : generate a molecule/molecules. \n'
             '[START_AMINO] : generate a protein annotation. \n'
    )
    
    parser.add_argument(
        '--max_length', type=int, default=70,
        help="Maximum length in tokens of the generated text including the prompt. "
             "If None, then 60 is used."
    )
    parser.add_argument(
        '--top_p', type=float, default=50,
        help="If specified performs top p sampling, i.e. samples from amongst the "
             "top tokens whose probabilities add up top_p. Gives more variability."
    )

    return parser.parse_args()


def galai_func(args):
    
    device = torch.device("cuda:3" if torch.cuda.is_available() else "cpu")

    loader = AutoLoader(task_name="lm",
                        model_name="galactica-1.3b-en",
                        model_dir="weights")

    model = loader.get_model()
    model.to(device)
    model.eval()

    tokenizer = loader.get_tokenizer()

    predictor = Predictor(model, tokenizer)

    text = args.prompt
    out = predictor.predict_generate_randomsample(text,
                                                out_max_length=args.max_length,
                                                top_k=args.top_p,
                                                repetition_penalty=1.2,
                                                temperature=0.7
                                                )


    if isinstance(out, list):
        for o in out:
            print(o)
    else:
        print(out)


def main():
    galai_func(process_args())


if __name__ == '__main__':
    main()