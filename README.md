# This is the landing page for docs.ansible.com

It is completely static so there is no "make" build process.  Just open the index.html file in a browser and start editing :).

There are two landing pages (index.html and ansible-tower/index.html) that may need editing:

	- index.html covers the main docsite landing page for both core and Tower documentation.
	- ansible-tower/index.html is the other landing page for Tower documentation.	

Once changes are saved, docsite needs to be rebuilt in Jenkins (Project Build_Docsite) for changes to populate online.
