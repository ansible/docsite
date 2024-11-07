# Stub pages

Stub pages are RST files that use the [`orphan` metadata field](https://www.sphinx-doc.org/en/master/usage/restructuredtext/field-lists.html#special-metadata-fields) so that the page is generated at build time but not included in the toctree.
The result is that the stub page does not appear in the navigation or documentation structure, while still being reachable from a direct external link such as a bookmark or reference in a third-party site.

## Overview

Stub pages provide an alternative to dynamic HTTP redirects that prevent 404 errors and broken links.
They have the following benefits:

- Avoid degradation of SEO authority and ensure that `docs.ansible.com` does not lose ranking with search engines.
- Allow community contributors to restructure documentation when access to server-side redirects is not available.
- Encourage users to update stale bookmarks and external links. This is arguably a disadvantage.
- Easier to maintain than redirects because there is no need for regex or special knowledge.

Stub pages also have some drawbacks:

- Dynamic redirects are more efficient for users because they do not require manual intervention to access pages that have been moved or removed.
- Stub pages add clutter to the source repository. A large number of unused files can be confusing for new contributors and more difficult to navigate. Although we can put most stubs in a special folder to avoid polluting other directories.
- Adds to the build time. While stub pages are not included in the toctree, they still need to be generated into HTML as part of the build.

### Background

So why do we need to create stub files in the first place?

Ansible community documentation that is available from `docs.ansible.com` has long been hosted on Red Hat managed infrastructure.
This infrastructue includes Apache httpd services with the `mod_rewrite` module that provides dynamic redirect functionality.
When pages in the Ansible package documentation were relocated or removed, a redirect rule was added to the `.htaccess` configuration file.
These files are sourced in the [ansible/docsite](https://github.com/ansible/docsite) repository.

To migrate hosting to ReadTheDocs, and provide greater access to community maintainers, a strategy is needed to prevent broken redirects that would result in 404s and degradation of SEO authority.
We can create some redirects in the ReadTheDocs project but there is a limit of 100 redirects per project.
Unfortunately the number of existing redirects already exceeds that limit.
Additionally, a goal is to move away from creating redirects because this adds a lot of maintenance overhead to the project.
The reasoning for the creation of many of the redirect rules in the `.htaccess` configuration files is historical knowledge with little no documentation.

Looking in the `.htaccess` file you can see rules such as this one:

```bash
RedirectMatch permanent "^/ansible/(devel|latest)/user_guide/playbooks_blocks.html" "https://docs.ansible.com/projects/ansible/$1/playbook_guide/playbooks_blocks.html" [R=301,L]
```

This redirect works for any links that are internal to the Ansible community documentation.
For instance, if a page references `user_guide/playbooks_blocks.html` the redirect will point to the corresponding page on ReadTheDocs.

However, if there is an external link such as a bookmark or reference from a third-party site, the redirect does not take effect because the `docs.ansible.com` subdomain has moved to ReadTheDocs.
As a result, that external link will cause a 404 error.
By using stub pages, we can prevent those 404s.

#### How stub pages work

On ReadTheDocs we have a top-level redirect in place that handles the new URL structure with the `/projects/` subfolder:

```text
Type: Exact Redirect
From URL: /ansible/*
To URL: /projects/ansible/:splat
Force Redirect: True
```

If an external link or bookmark references `https://docs.ansible.com/ansible/latest/user_guide/playbooks_blocks.html` then this redirect points to the following url:

```text
https://docs.ansible.com/projects/ansible/latest/user_guide/playbooks_blocks.html
```

In this case, there is a [stub page](https://raw.githubusercontent.com/ansible/ansible-documentation/refs/heads/devel/docs/docsite/rst/user_guide/playbooks_blocks.rst) that opens and informs the user that the page has moved.
You can view the [`user_guide/playbooks_blocks.html`](https://ansible.readthedocs.io/projects/ansible/latest/user_guide/playbooks_blocks.html) stub page on ReadTheDocs now.

## Stubs that do not exist

Stub pages in this section do not exist in the `ansible-documentation` repository and need to be added.

### Getting started

/ansible/(devel|latest)/intro_getting_started.html
/ansible/(devel|latest)/intro.html
/ansible/(devel|latest)/quickstart.html

### Command line tools

/ansible/(devel|latest)/command_line_tools.html
/ansible/(devel|latest)/user_guide/command_line_tools.html
/ansible/(devel|latest)/intro_adhoc.html

### CLI guides

/ansible/(devel|latest)/ansible.html
/ansible/(devel|latest)/ansible-vault.html
/ansible/(devel|latest)/ansible-pull.html
/ansible/(devel|latest)/ansible-playbook.html
/ansible/(devel|latest)/ansible-inventory.html
/ansible/(devel|latest)/ansible-galaxy.html
/ansible/(devel|latest)/ansible-doc.html
/ansible/(devel|latest)/ansible-console.html
/ansible/(devel|latest)/ansible-config.html

### Vault guide

/ansible/(devel|latest)/playbooks_vault.html
/ansible/(devel|latest)/vault.html

### Modules and plugins

/ansible/(devel|latest)/modules.html
/ansible/(devel|latest)/modules_intro.html
/ansible/(devel|latest)/modules_support.html
/ansible/(devel|latest)/plugin_filtering_config.html
/ansible/latest/modules.html

### Installation guide

/ansible/(devel|latest)/intro_configuration.html
/ansible/(devel|latest)/intro_installation.html

### Inventory guide

/ansible/(devel|latest)/intro_inventory.html
/ansible/(devel|latest)/intro_patterns.html
/ansible/(devel|latest)/intro_dynamic_inventory.html

### Module list landing topics

/ansible/(devel|latest)/network_maintained.html
/ansible/(devel|latest)/partner_maintained.html
/ansible/(devel|latest)/community_maintained.html
/ansible/(devel|latest)/core_maintained.html
/ansible/(devel|latest)/list_of_windows_modules.html
/ansible/(devel|latest)/list_of_web_infrastructure_modules.html
/ansible/(devel|latest)/list_of_utilities_modules.html
/ansible/(devel|latest)/list_of_system_modules.html
/ansible/(devel|latest)/list_of_storage_modules.html
/ansible/(devel|latest)/list_of_source_control_modules.html
/ansible/(devel|latest)/list_of_remote_management_modules.html
/ansible/(devel|latest)/list_of_packaging_modules.html
/ansible/(devel|latest)/list_of_notification_modules.html
/ansible/(devel|latest)/list_of_network_modules.html
/ansible/(devel|latest)/list_of_net_tools_modules.html
/ansible/(devel|latest)/list_of_monitoring_modules.html
/ansible/(devel|latest)/list_of_messaging_modules.html
/ansible/(devel|latest)/list_of_inventory_modules.html
/ansible/(devel|latest)/list_of_identity_modules.html
/ansible/(devel|latest)/list_of_files_modules.html
/ansible/(devel|latest)/list_of_database_modules.html
/ansible/(devel|latest)/list_of_crypto_modules.html
/ansible/(devel|latest)/list_of_commands_modules.html
/ansible/(devel|latest)/list_of_clustering_modules.html
/ansible/(devel|latest)/list_of_cloud_modules.html
/ansible/(devel|latest)/list_of_all_modules.html

### Networking guide

/ansible/(devel|latest)/network_best_practices_2.5.html
/ansible/(devel|latest)/network_debug_troubleshooting.html
/ansible/(devel|latest)/network_working_with_command_output.html
/ansible/(devel|latest)/network.html
/ansible/(devel|latest)/intro_networking.html

### Plugins list

/ansible/(devel|latest)/plugins.html

### Porting guide

/ansible/(devel|latest)/porting_guide_2.0.html
/ansible/(devel|latest)/porting_guide_2.3.html
/ansible/(devel|latest)/porting_guide_2.4.html
/ansible/(devel|latest)/porting_guide_2.5.html
/ansible/(devel|latest)/porting_guides.html

### Reference and appendices

/ansible/(devel|latest)/common_return_values.html
/ansible/(devel|latest)/config.html
/ansible/(devel|latest)/faq.html
/ansible/(devel|latest)/galaxy.html
/ansible/(devel|latest)/reference_appendices/galaxy.html
/ansible/(devel|latest)/glossary.html
/ansible/(devel|latest)/guide_aci.html
/ansible/(devel|latest)/playbooks_keywords.html
/ansible/(devel|latest)/python_3_support.html
/ansible/(devel|latest)/release_and_maintenance.html
/ansible/(devel|latest)/test_strategies.html
/ansible/(devel|latest)/tower.html
/ansible/(devel|latest)/YAMLSyntax.html

### Scenario Guides

/ansible/(devel|latest)/guide_aws.html
/ansible/(devel|latest)/guide_azure.html
/ansible/(devel|latest)/guide_cloudstack.html
/ansible/(devel|latest)/guide_docker.html
/ansible/(devel|latest)/guide_gce.html
/ansible/(devel|latest)/guide_kubernetes.html
/ansible/(devel|latest)/guide_packet.html
/ansible/(devel|latest)/guide_rax.html
/ansible/(devel|latest)/guide_rolling_upgrade.html
/ansible/(devel|latest)/guide_vagrant.html
/ansible/(devel|latest)/guide_vmware.html
/ansible/(devel|latest)/guides.html
/ansible/(devel|latest)/scenario_guides/guide_rolling_upgrade.html
/ansible/(devel|latest)/vmware/scenarios.html
/ansible/(devel|latest)/vmware/faq.html
/ansible/(devel|latest)/vmware/index.html
/ansible/(devel|latest)/vmware/vmware_?(.+)?
/ansible/(devel|latest)/vmware/scenario_?(.+)?

### Renamed module reference directory

/ansible/(devel|latest)/modules_by_category.html
/ansible/(devel|latest)/modules/modules_by_category.html

### Community page

/ansible/(devel|latest)/community.html

### Windows and BSD guide

/ansible/(devel|latest)/windows.html
/ansible/(devel|latest)/intro_bsd.html
/ansible/(devel|latest)/intro_windows.html
/ansible/(devel|latest)/windows_dsc.html
/ansible/(devel|latest)/windows_faq.html
/ansible/(devel|latest)/windows_setup.html
/ansible/(devel|latest)/windows_usage.html
/ansible/(devel|latest)/windows_winrm.html

### Not devel or latest version files

Some files in the redirects are non-versioned or specific to older versions.
Maybe these should be ported to ReadTheDocs redirects or just dropped.

/ansible/(developing_[^/]+)\.html
/ansible/developing.html
/ansible/dev_guide(\/)?
/ansible/modules_by_category.html
/ansible/community.html
/ansible/modules.html

#### Redirects a full directory

/ansible/(devel|latest)/module_docs/?(.+)?

#### Pages moved in older versions, 2.5 and 2.6

/ansible/([^/]+)/user_guide/playbooks_vault.html
/ansible/([^/]+)/user_guide/quickstart.html
/ansible/([^/]+)/vmware/index.html

#### Related to PR 74834 (link still exists in 2.9 error messages)

/ansible/playbooks_vault.html
/ansible/network_debug_troubleshooting.html

### Playbook guide

/ansible/(devel|latest)/playbooks.html
/ansible/(devel|latest)/become.html
/ansible/(devel|latest)/playbooks_advanced_syntax.html
/ansible/(devel|latest)/playbooks_async.html
/ansible/(devel|latest)/playbooks_best_practices.html
/ansible/(devel|latest)/playbooks_blocks.html
/ansible/(devel|latest)/playbooks_checkmode.html
/ansible/(devel|latest)/playbooks_conditionals.html
/ansible/(devel|latest)/playbooks_debugger.html
/ansible/(devel|latest)/playbooks_delegation.html
/ansible/(devel|latest)/playbooks_environment.html
/ansible/(devel|latest)/playbooks_error_handling.html
/ansible/(devel|latest)/playbooks_filters_ipaddr.html
/ansible/(devel|latest)/playbooks_filters.html
/ansible/(devel|latest)/playbooks_intro.html
/ansible/(devel|latest)/playbooks_lookups.html
/ansible/(devel|latest)/playbooks_loops.html
/ansible/(devel|latest)/playbooks_prompts.html
/ansible/(devel|latest)/playbooks_reuse_includes.html
/ansible/(devel|latest)/playbooks_reuse_roles.html
/ansible/(devel|latest)/playbooks_reuse.html
/ansible/(devel|latest)/playbooks_startnstep.html
/ansible/(devel|latest)/playbooks_strategies.html
/ansible/(devel|latest)/playbooks_tags.html
/ansible/(devel|latest)/playbooks_tests.html
/ansible/(devel|latest)/playbooks_variables.html
/ansible/(devel|latest)/playbook_pathing.html
/ansible/(devel|latest)/playbooks_python_version.html
/ansible/(devel|latest)/playbooks_roles.html
/ansible/(devel|latest)/playbooks_special_topics.html
/ansible/(devel|latest)/playbooks_templating.html

## Stubs that already exist

Stub pages in this section already exist in the `ansible-documentation` repository.

### User guide

/ansible/(devel|latest)/user_guide/basic_concepts.html
/ansible/(devel|latest)/user_guide/intro_getting_started.html
/ansible/(devel|latest)/user_guide/intro.html
/ansible/(devel|latest)/user_guide/quickstart.html
/ansible/(devel|latest)/user_guide/intro_adhoc.html
/ansible/(devel|latest)/user_guide/cheatsheet.html
/ansible/(devel|latest)/user_guide/vault.html
/ansible/(devel|latest)/user_guide/modules.html
/ansible/(devel|latest)/user_guide/modules_intro.html
/ansible/(devel|latest)/user_guide/modules_support.html
/ansible/(devel|latest)/user_guide/plugin_filtering_config.html
/ansible/(devel|latest)/user_guide/collections_using.html
/ansible/(devel|latest)/user_guide/sample_setup.html
/ansible/(devel|latest)/user_guide/connection_details.html
/ansible/(devel|latest)/user_guide/intro_inventory.html
/ansible/(devel|latest)/user_guide/intro_patterns.html
/ansible/(devel|latest)/user_guide/intro_dynamic_inventory.html
/ansible/(devel|latest)/user_guide/windows_performance.html
/ansible/(devel|latest)/user_guide/windows.html
/ansible/(devel|latest)/user_guide/intro_bsd.html
/ansible/(devel|latest)/user_guide/intro_windows.html
/ansible/(devel|latest)/user_guide/windows_dsc.html
/ansible/(devel|latest)/user_guide/windows_faq.html
/ansible/(devel|latest)/user_guide/windows_setup.html
/ansible/(devel|latest)/user_guide/windows_usage.html
/ansible/(devel|latest)/user_guide/windows_winrm.html
/ansible/(devel|latest)/user_guide/complex_data_manipulation.html
/ansible/(devel|latest)/user_guide/playbooks_module_defaults.html
/ansible/(devel|latest)/user_guide/playbooks_vars_facts.html
/ansible/(devel|latest)/user_guide/playbooks.html
/ansible/(devel|latest)/user_guide/become.html
/ansible/(devel|latest)/user_guide/playbooks_advanced_syntax.html
/ansible/(devel|latest)/user_guide/playbooks_async.html
/ansible/(devel|latest)/user_guide/playbooks_best_practices.html
/ansible/(devel|latest)/user_guide/playbooks_blocks.html
/ansible/(devel|latest)/user_guide/playbooks_checkmode.html
/ansible/(devel|latest)/user_guide/playbooks_conditionals.html
/ansible/(devel|latest)/user_guide/playbooks_debugger.html
/ansible/(devel|latest)/user_guide/playbooks_delegation.html
/ansible/(devel|latest)/user_guide/playbooks_environment.html
/ansible/(devel|latest)/user_guide/playbooks_error_handling.html
/ansible/(devel|latest)/user_guide/playbooks_filters_ipaddr.html
/ansible/(devel|latest)/user_guide/playbooks_filters.html
/ansible/(devel|latest)/user_guide/playbooks_intro.html
/ansible/(devel|latest)/user_guide/playbooks_lookups.html
/ansible/(devel|latest)/user_guide/playbooks_loops.html
/ansible/(devel|latest)/user_guide/playbooks_prompts.html
/ansible/(devel|latest)/user_guide/playbooks_reuse_includes.html
/ansible/(devel|latest)/user_guide/playbooks_reuse_roles.html
/ansible/(devel|latest)/user_guide/playbooks_reuse.html
/ansible/(devel|latest)/user_guide/playbooks_startnstep.html
/ansible/(devel|latest)/user_guide/playbooks_strategies.html
/ansible/(devel|latest)/user_guide/playbooks_tags.html
/ansible/(devel|latest)/user_guide/playbooks_tests.html
/ansible/(devel|latest)/user_guide/playbooks_variables.html
/ansible/(devel|latest)/user_guide/playbook_pathing.html
/ansible/(devel|latest)/user_guide/playbooks_python_version.html
/ansible/(devel|latest)/user_guide/playbooks_roles.html
/ansible/(devel|latest)/user_guide/playbooks_special_topics.html
/ansible/(devel|latest)/user_guide/playbooks_templating.html

### Developer

/ansible/(devel|latest)/dev_guide/testing_compile.html
