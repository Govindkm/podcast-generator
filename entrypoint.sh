#!/bin/bash

echo "Starting the application..."
git config --global user.name "${GITHUB_ACTOR}"
git config --global user.email "${INPUT_EMAIL}"
git config --global --add safe.directory /github/workspace

apt-get insall python3

python /usr/bin/feed.py

git add .
git commit -m "Update feed"
git push --set-upstream origin "${GITHUB_REF}" --force
if [ $? -ne 0 ]; then
    echo "Error: Failed to push changes to the repository."
    exit 1
fi
echo "Changes pushed successfully."

echo "Application finished."