import argparse
from src.data.main import data_main
from src.features.main import features_main
from src.models.main import models_main
from src.visualization.main import visualization_main


# create the top-level parser
parser = argparse.ArgumentParser()

# Creation of subparsers Add and Deploy
subparsers = parser.add_subparsers(
    help='Differentiate between data, features, models and visualizations commands',
    dest="subparser"
)

parser_add = subparsers.add_parser('data', help='Data related commands')
parser_add.add_argument('--download',
                        default='lorem',
                        choices=['lorem'],
						help="Download the dataset",
)

parser_features = subparsers.add_parser(
	'features', help='Features related commands')

parser_models = subparsers.add_parser(
	'models', help='Models related commands')

parser_features = subparsers.add_parser(
	'visualization', help='Visualization related commands')



# Parsing args
args = parser.parse_args()

if args.subparser == "data":
	if args.download == 'lorem':
		data_main()
elif args.subparser == "features":
	features_main()
elif args.subparser == "models":
	models_main()
elif args.subparser == "visualization":
	visualization_main()