# encoding: utf-8

""" Extract archive files.
    Handles tar and zip.
"""

import tarfile
import zipfile


def find_type(archive_path): #{{{
    """ See if the file is actually an archive. """

    extension = archive_path.split(".")[-1].lower()

    if extension in ['tar', 'bz2', 'gz', 'gzip']:
        if tarfile.is_tarfile(archive_path):
            return ('tar', extension)

    elif extension == 'zip':
        if zipfile.is_zipfile(archive_path):
            return ('zip',) #}}}


def check_for_bad_filenames(names_list): #{{{
    """ Look for Malicious filenames in the archive.
        Throw an exception if we find any.
    """
    for name in names_list:
        if name.startswith('/'):
            raise Exception('Malicous filenames in this archive!')
        for level in name.split('/'):
            if '..' in level:
                raise Exception('Malicous filenames in this archive!') #}}}


def extract_tar(archive_path, comp_type, extract_path): #{{{
    """ Extract a tar archive. """

    tar_file = tarfile.open(archive_path,
            'r:{comp_type}'.format(comp_type=comp_type))

    check_for_bad_filenames(tar_file.getnames())

    tar_file.extractall(extract_path)
    tar_file.close() #}}}


def extract_zip(archive, extract_path): #{{{
    """ Extract a zip archive. """
    zip_file = zipfile.ZipFile(archive, 'r')

    check_for_bad_filenames(zip_file.namelist())

    zip_file.extractall(extract_path)
    zip_file.close() #}}}


def extract_archive(archive_path, extract_path): #{{{
    """ Extract an archive to the specified path. """

    archive_type = find_type(archive_path)

    if archive_type[0] != None:
        if archive_type[0] == 'tar':
            extract_tar(archive_path, archive_type[1], extract_path)
        elif archive_type[0] == 'zip':
            extract_zip(archive_path, extract_path)
    else:
        print 'Bad archive!' #}}}
