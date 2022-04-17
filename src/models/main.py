import pytorch_lightning as pl


def models_main(cfg, data):
	dict_args = vars(args)
	if args.embeddings:
		print(f"{args.train_dir = }")
		dm = DM_Embeddings(args.train_dir)
		if args.embeddings == "n-gram":
			model = Embedding_W2V_CBOW(**dict_args)
		elif args.embeddings == "cbow":
			model = Embedding_W2V_CBOW(**dict_args)
	elif args.vic_from_picks:
		prep = "None"
		input_size = {
			"None": 1
		}
		dm = DM_LSTM(args.train_dir, prep)
		if args.vic_from_picks == "random":
			pass
		elif args.vic_from_picks == "naive-bayes":
			pass
		elif args.vic_from_picks == "lstm":
			model = OurMagnicientLSTM(input_size[prep], **dict_args)
		pass
	else:
		return
	trainer = pl.Trainer.from_argparse_args(args, gpus=1, max_epochs=50)
	trainer.fit(model, datamodule=dm)
	_ = trainer.test(model, datamodule=dm)
