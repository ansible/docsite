# Landing pages for docs.ansible.com

To update or add content, open the relevant ``data/*.yaml`` file with any text editor.

To build the docsite locally, do the following:

1. Install the requirements.
    ```
    python -m pip install -r requirements.in -c requirements.txt
    ```
2. Build the docsite.
    ```
    python build.py
    ```

You can find the generated HTML and other assets in the ``output`` folder.

Want to make some changes?

Fork this repo and show us what you've got.
You can also head over to the [DaWGs](https://matrix.to/#/#docs:ansible.com) room and share your thoughts with the Ansible community on Matrix.
