#!/bin/bash
# Copy all course materials to docs folder
cd /Users/maria.talvik/claude-projects/automation/automation

# Create docs directories if needed
for dir in ansible_basics ansible_advanced ansible_roles docker_fundamentals docker_orchestration git_version_control kubernetes_overview terraform_basics ci_cd_advanced
do
  if [ -d "$dir" ] && [ ! -d "docs/$dir" ]; then
    cp -r "$dir" "docs/"
    echo "Copied $dir to docs/"
  fi
done

echo "All course materials copied to docs folder!"
