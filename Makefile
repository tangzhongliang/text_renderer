gen-eng:
	python main.py --config_file configs/default_test.yaml --output_dir output --tag eng --corpus_mode eng --chars_file data/chars/eng.txt --corpus_dir data/corpus/words.txt --fonts_list data/fonts/eng,data/fonts/chn --length 10 --clip_max_chars --strict --space_ratio 0 --num_img 200

gen-chn:
	python main.py --config_file configs/default_test.yaml --output_dir output --tag chn --corpus_mode random --fonts_list data/fonts/chn --strict --space_ratio 0 --num_img 100

.PHONY: gen-eng gen-chn
