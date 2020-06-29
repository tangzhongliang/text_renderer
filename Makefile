gen-number:
	python main.py --config_file configs/default_test.yaml --output_dir output --tag number --corpus_mode random --chars_file data/chars/number.txt --fonts_list data/fonts/eng --length 20 --clip_max_chars --strict --space_ratio 0 --num_img 20

gen-eng:
	python main.py --config_file configs/default_test.yaml --output_dir output --tag eng --corpus_mode eng --chars_file data/chars/eng.txt --corpus_dir data/corpus/words.txt --fonts_list data/fonts/eng,data/fonts/chn --length 20 --clip_max_chars --strict --space_ratio 0 --gpu --num_img 20

gen-chn:
	python main.py --config_file configs/default_test.yaml --output_dir /root/data/gen_images --tag chn --corpus_mode random --fonts_list data/fonts/chn --length 10 --strict --space_ratio 0 --gpu --num_img 3000000

.PHONY: gen-number gen-eng gen-chn
