#!/bin/bash

usage() {
      echo "Usage:"
      echo "    ./tests.sh -h|--help                        Display this help message."
      echo "    ./tests.sh -i <path to yaml item file>      Init tests : prepare env tests"
      echo "    ./tests.sh --all                            Run all tests"
      echo "    ./tests.sh --single                         Run single test : ./tests.sh --single <MYPATH/config.yaml>"

      exit 0  
}

init_tests() {
    git clone https://github.com/crowdsecurity/hub-tests.git
    cd hub-tests/ && go build && cd ..
    cp -r hub-tests/config/ .
    mkdir config/hub && cp .index.json config/hub/
    mkdir data
    if [[ -n  $1 ]];
    then
	TEST=$1
	ITEM_TYPE=$(echo $TEST | awk -F "/" '{print $1}')
	ITEM_NAME=$(echo $TEST | awk -F "/" '{print $(NF-1)"/"$(NF)}')
	ITEM_NAME=$(echo $ITEM_NAME | awk -F "." '{print $1}')
	mkdir -p $(dirname $TEST)/.tests/$(basename $TEST .yaml)
	cat <<EOF > $(dirname $TEST)/.tests/$(basename $TEST .yaml)/config.yaml
log_file:  auth.log #unused for now, will need rework when acquis.yaml will part of parsers
parser_results: pars   er_results.json
bucket_input: bucket_input.yaml
bucket_results: bucket_result.json
postoverflow_input: postoverflow_input.yaml
postoverflow_results: postoverflow_results.json
#configuration
index: "./config/hub/.index.json"
configurations:
  $ITEM_TYPE:
  - $ITEM_NAME
EOF
    fi
}

run_all_tests() {
    ./hub-tests/hub-tests -glob config.yaml
}

run_single_test() {
    ./hub-tests/hub-tests -single $1
}

if [[ $# -eq 0 ]]; then
usage
fi

while [[ $# -gt 0 ]]
do
    key="${1}"
    case ${key} in
    -i)
        init_tests ${2}
        exit 0
        ;;
    --all)
        run_all_tests
        exit 0
        ;;
    --single)
        run_single_test ${2}
        exit 0
        ;;
    -h|--help)
        usage
        exit 0
        ;;
    *)    # unknown option
        echo "Unknown argument ${key}."
        usage
        exit 1
        ;;
    esac
done
