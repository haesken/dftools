# dfpm package format

    gz (outer file)
        \
        package.tar
            \
            package folder
                \
                files

        meta.tar
            \
            meta.json

# meta.json format

    {
        "package-info" {
            "name": "example"
            "version": "major.minor.patch"
            "author-name": "name"
            "author-email": "example@example.com"
            "maintainer": "name"
            "maintainer-email": "example@example.com"
            "git-urls": [
                "git://github.com/user/repo.git"
            ]
        }
        "dfopt-manifest" {
            "option-name" [
                "option-value"
            ]
        }
    }

