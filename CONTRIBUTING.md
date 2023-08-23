# Contributing

Hello. This is the place where you can contribute ideas for an update to the Ansible docsite.

We love it when people submit new ideas, make improvements, and fix our mistakes. So welcome!

## Things to know before your first contribution

- All code and doc submissions are done through pull requests against the `main` branch.
- We ask all of our community members and contributors to adhere to the [Ansible code of conduct]. If you have questions, or need assistance, please reach out to our community team at [codeofconduct@ansible.com].

## Building the docsite locally

To update or add content, open the relevant ``data/*.yaml`` file with any text editor.

To build the docsite locally and verify your changes, do the following:

```sh
python -m pip install -r requirements.in -c requirements.txt
python build.py
```

You can find generated HTML and other assets in the ``output`` folder.

[Ansible code of conduct]: https://docs.ansible.com/ansible/latest/community/code_of_conduct.html
[codeofconduct@ansible.com]: mailto:codeofconduct@ansible.com
