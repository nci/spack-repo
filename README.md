# NCI Spack packages

This is the spack package repository maintained by NCI for packages that are not available from  spack built-in repo. It only supports NCI build use-cases.

To use it, firstly run:

`git clone https://github.com/nci/spack-repo.git`

and then add the location of the cloned repository to your spack instance:

`spack repo add $PACKAGE_PATH/spack-reoo`

Finally you can  confirm it is has been added correctly:

```
$ spack repo list
==> 2 package repositories.
nci           $PACKAGE_PATH/spack-repo
builtin       $SPACK_ROOT/var/spack/repos/builtin
```

Now the fiat package should be available to install
```
$ spack list fiat
fiat  py-fenics-fiat
==> 2 packages
```

# More information
For more information see the extensive spack documentation on how to utilise repository files.

