# Ansible user journey maps

This document extends Ansible docsite personas by identifying and describing their automation journeys.

[Ansible docsite personas](docsite-personas.md)

## Intro

Each persona has specific milestones in their automation journey.
And each milestone has specific major actions that the persona achieves.
The first milestone of each journey starts with human motivation.

```yaml
Milestone: Aware
  Major action
  Major action
  ...
Milestone: Evaluate
  Major action
  Major action
  ...
Milestone: Adopt
  Major action
  Major action
  ...
Milestone: Scale
  Major action
  Major action
  ...
```

## Novice

```yaml
Milestone: Need to learn the basics
  Understand the challenges of modern infrastructure management [content gap]
  Understand the fundamentals of Ansible automation
Milestone: Set up an automation project
  Install the Ansible package
  Create a basic inventory file
  Run an ad-hoc command
Milestone: Write first playbook
  Create a hello world playbook
  Run the playbook with the ansible-playbook command
```

## User

```yaml
Milestone: Have something to automate
  Start writing playbooks
  Evaluate plugins to see if results of execution meet needs
Milestone: Learn inventories
  Create an inventory file to manage multiple hosts
  Use dynamic inventories
Milestone: Organize the automation project as it starts to grow
  Use roles to structure the automation project
Milestone: Improve automation content
  Install developer tools (ansible-lint, vscode extension, molecule)
Milestone: Re-use existing automation content
  Start exploring Ansible Galaxy
  Install and use roles and/or collections
  Customize automation content
Milestone: Share automation content
  Submit roles to an existing collection
  Create a collection and upload to Galaxy
Milestone: Use AWX for more convenient automation
  Execute automation jobs on demand with the REST API or Web UI
  Schedule automation jobs
  Create AWX job templates
Milestone: Use Ansible Runner / Ansible SDK as an interface for automation
  Build execution environment with specific dependencies
  Use execution environments with AWX jobs
```

## Developer

```yaml
Milestone: Become interested in writing code for Ansible
  Set up development environment
  Review code of conduct and contributor guidelines
Milestone: Contribute to an Ansible project
  Review issues and PRs in an Ansible project
  Fix issues and implement new features in an Ansible project, collection, or module
Milestone: Test changes to plugins and modules
  Understand testing in Ansible
  Run sanity tests
  Write integration tests
  Write unit tests
Milestone: Create a new collection
  Use the collection skeleton
  Use GitHub actions to set up testing workflows
  Troubleshoot collections with ansible-navigator
  Request a collection be added to the Ansible package
```

## Community maintainer

```yaml
Milestone: Oversee the regular maintenance and updates to a collection
  Overview of what maintenance means in general
Milestone: Learn maintainer responsibilities
  Use existing communication channels, create new channels
  Ensure CI is working and relevant
  Review, merge and backport changes
  Release the project
  Maintain good collection documentation
Milestone: Expand community around a collection
Milestone: Get collection included in the Ansible package
  Understand the inclusion process
  Go through inclusion review cycles
Milestone: Participate in higher-level cross-project governance
  Join the Ansible steering committee
```

## Community member

```yaml
Milestone: Become interested in joining the community
  Learn about the Ansible community and its purpose
  Review and agree to the code of conduct
  Join or initiate a discussion
Milestone: Start actively participating in the Ansible community
  Participate in a meetup or other local event
  Contribute to an Ansible project
Milestone: Expand Ansible community activities
  Present at a meetup
  Write and share blog post or YouTube video, etc.
Milestone: Become an Ansible community evangelist
  Host an Ansible meetup
  Become a maintainer of an Ansible project or collection
  Join the Ansible steering committee
```
