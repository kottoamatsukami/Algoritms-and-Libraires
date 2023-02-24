import subprocess
import os
import git
import shutil
import stat


class LibManager:
    def __init__(self, libs: dict) -> None:
        self.libs = libs
        self.searched = []

    def setup_libs(self):
        for i, lib in enumerate(self.libs):
            print(f"{i+1}) <{lib}:{self.libs[lib][0]}>")
            type_ = self.libs[lib][0]
            if type_ == "pip":
                subprocess.run(
                    f"pip install {lib}"
                )
            elif type_ == "github":
                temp_path = os.path.join(os.curdir, "temp")
                if not os.path.exists(temp_path):
                    os.mkdir(temp_path)
                git.Repo.clone_from(
                    self.libs[lib][1],
                    temp_path,
                )
                out = self.search_dir(
                    name=lib,
                    pth=temp_path,
                )
                self.expand(out)
                if len(self.searched) == 0:
                    raise ValueError(f"{lib} does not exist")
                pth = sorted(self.searched, key=len)[0]
                if os.path.exists(self.libs[lib][2]):
                    self.del_dir(self.libs[lib][2])
                shutil.copytree(
                    src=pth,
                    dst=self.libs[lib][2],
                )
                self.del_dir(temp_path)

    def del_dir(self, pth):
        if os.path.isdir(pth):
            for next_dir in os.listdir(pth):
                self.del_dir(os.path.join(pth, next_dir))
            os.rmdir(pth)
        else:
            os.chmod(pth, stat.S_IWRITE)
            os.remove(pth)

    def search_dir(self, name, pth):
        out = []
        if os.path.isdir(pth):
            if name == pth.split('\\')[-1]:
                return pth
            for next_dir in os.listdir(pth):
                out.append(self.search_dir(name, os.path.join(pth, next_dir)))
        return out

    def expand(self, *args):
        for arg in args:
            if isinstance(arg, list):
                self.expand(*arg)
            else:
                self.searched.append(arg)
