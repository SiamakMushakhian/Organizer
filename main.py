from pathlib import Path
import shutil

class OrganizeDir:
    """Class to organize files in a directory. 

    Example:
    >>> organizer = OrganizDir()
    >>> organizer.run(to_organize_directory)
    """
    suffix_dir = {
        '.png' : 'images',
        '.jpg' : 'images',
        '.jpeg' : 'images',
        '.txt' : 'docs',
        '.pdf' : 'docs',
        '.csv' : 'docs',
        '.zip' : 'compressed',
        '.rar' : 'compressed',
        '.py' : 'python',
        '.ipynb' : 'python',
        '.deb' : 'executable',
        '.app' :'other',
        '.dmg' : 'other',
        '.pth' : 'other'
    }

    def run(self, to_organize_dir: str):
        """Runs organizer job to move files to the specified destinations in suffix_dir.

        :param to_organize_dir: Directory to run organization job
        """
        self.to_organize_dir = Path(to_organize_dir)
        assert self.to_organize_dir.exists(), f'Directory: "{self.to_organize_dir}" not found'

        # iterate over files to organize
        for path in self.to_organize_dir.iterdir():

            if path.is_dir():
                # to avoid moving directories created by us
                if path.name in OrganizeDir.suffix_dir.values():
                    continue

                dest = 'dirs'
                DEST_DIR = self.to_organize_dir / dest
                DEST_DIR.mkdir(exist_ok=True)
                shutil.move(str(path), str(DEST_DIR))

            elif path.is_file():
                suffix = path.suffix
                dest = OrganizeDir.suffix_dir.get(suffix)

                # suffix is not supported yet
                # does not exist in suffix_dir
                if not dest:
                    continue

                DEST_DIR = self.to_organize_dir / dest
                DEST_DIR.mkdir(exist_ok=True)
                shutil.move(str(path), str(DEST_DIR))

if __name__ == '__main__':
    # HOME_DIR = Path.home()
    HOME_DIR = Path('/mnt/c/Users/siama/Downloads')
    organizer = OrganizeDir()
    organizer.run(HOME_DIR)

