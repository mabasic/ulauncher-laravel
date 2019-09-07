EXT_NAME:=ulauncher-laravel
EXT_DIR:=$(shell pwd)

attach:
	@ln -s ${EXT_DIR} ~/.cache/ulauncher_cache/extensions/${EXT_NAME}

detach:
	@rm -r ~/.cache/ulauncher_cache/extensions/${EXT_NAME}
