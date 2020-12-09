#!/bin/bash

usage() {
      echo "Usage:"
      echo "    ./tests.sh -h|--help                        Display this help message."
      echo "    ./tests.sh -i                               Init tests : prepare env tests"
      echo "    ./tests.sh --all                            Run all tests"
      echo "    ./tests.sh --single                         Run single test : ./tests.sh --single <MYPATH/config.yaml>"

      exit 0  
}

init_tests() {
    git clone https://github.com/crowdsecurity/hub-tests.git
    cd hub-tests/ && go build && cd ..
    cp -r hub-tests/config/ .
    mkdir config/hub && cp .index.json config/hub/
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
        init_tests
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
