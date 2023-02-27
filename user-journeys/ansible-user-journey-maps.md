# Ansible user journey maps

This document extends Ansible personas by identifying and describing their automation journey milestones.

Ansible community personas: https://github.com/ansible/docsite/blob/personas/personas/ansible-docsite-personas.md

## Novice

```yaml
Milestone: Learn the basics
  Understand the fundamentals of Ansible automation
  Install the Ansible package and run a hello world playbook
Milestone: Set up an automation project
  Create a Python virtual environment
  Install additional Ansible dev tools
  Create an inventory of managed nodes
```

## User

```yaml
Milestone: Start writing playbooks
  Learn about recommended tools for playbook quality (ansible-lint, handlers, etc)
  Start validating playbooks
Milestone: Make playbooks reusable
  Organize the automation project as it grows.
  Use roles to structure the automation project.
  Use Ansible Molecule to improve role quality.
Milestone: Create execution environment
Milestone: Execute playbooks remotely
  Use the AWX REST API.
  Use the AWX Web UI.
  Run playbooks on a cron.
Milestone: Share automation
  Contribute to a collection.
  Create a collection.
  Allow others to run the playbook.
  Create AWX job templates.
```

## Operations

```yaml
Milestone: Perform updates in production environments
  Check the porting guides.
Milestone: Manage multiple playbooks, inventories, and jobs with AWX
Milestone: Stand up private Galaxy instance
```

## Developer

```yaml
Milestone: Learn how to contribute code
  Review code of conduct and contributor guidelines
  Review PRs in an Ansible project
  Fix issues in an Ansible project, collection, or module
Milestone: Create module or plugin
Milestone: Add to existing collection
  Include a new module
  Deprecate a module
Milestone: Convert role to collection
Milestone: Create a new collection
  Troubleshoot collections with ansible-navigator
  Request a collection be added to the Ansible package
Milestone: Use event-driven automation
```

## Community maintainer

```yaml
Milestone: Actively participate in the Ansible community
  Follow community-related discussions and participate in decisions
Milestone: Manage the Ansible project
  Ensure important issues are fixed
  Release project/collections regularly
  Oversee CI workflows, PR reviews and merges
Milestone: Foster community of contributors
```

## Community member

```yaml
Milestone: Become interested in joining the community
  Learn about the Ansible community and its purpose
  Review and agree to the code of conduct
  Join or initiate a discussion
  Participate in a meetup or other local event
  Contribute to an Ansible project
Milestone: Expand Ansible community activities
  Presents at a meetup
  Writes and shares blog post/video etc
  Contributes a feature/collection etc to an Ansible project
Milestone: Become an Ansible community evangelist
  Host Ansible meetups
  Become a maintainer of an Ansible project or collection
  Become a member of Ansible steering committee
```