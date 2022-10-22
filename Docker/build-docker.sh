#!/usr/bin/env bash
# A simple script for building a development version of the container

export BUILD_OUTPUT_FILE=./output_build.txt
export CONTAINER_TAG=sk8forether/trans-game-dev
echo "**Trans Game Docker** Build started, output in ${BUILD_OUTPUT_FILE}"

# Uncomment to save build output log instead of printing to the screen
#docker build --network=host --tag ${CONTAINER_TAG} ./ 2>&1 > $BUILD_OUTPUT_FILE

# Uncomment to save build output log AND print to screen
docker build --network=host --tag ${CONTAINER_TAG} 2>&1 | tee $BUILD_OUTPUT_FILE

# Some useful summary output
echo "-------------------------------------------------------------"
echo "Build complete.  Check output file for final status.  Possible Errors:"
cat $BUILD_OUTPUT_FILE | grep ERROR
cat $BUILD_OUTPUT_FILE | grep Error
echo "-------------------------------------------------------------"
echo "Tail of build output file:"
cat $BUILD_OUTPUT_FILE | tail
