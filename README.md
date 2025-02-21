

# wmiclient / wmic for Linux

wmi 1.3.16 source code for Linux

This project is derived from the original package available at  
[Opsview](http://www.opsview.com/sites/default/files/wmi-1.3.16.tar_.bz2)  
and based on the discussion at  
[Ask Ubuntu](https://askubuntu.com/questions/885407/installing-wmic-on-ubuntu-16-04-lts).  
I modified the code to be compatible with newer versions of GnuTLS.

Below are the instructions to build and install wmiclient from scratch (tested on Ubuntu 18.04 and later).

---

## Prerequisites

Before starting, install the necessary packages. Open a terminal and run:

```bash
sudo apt update
sudo apt install autoconf gcc libdatetime-perl make build-essential g++ python-dev python2
```

> **Note:**  
> Some systems may not have `/usr/bin/python` by default.  
> If after installing you get an error about missing Python, create a symbolic link so that `/usr/bin/python` points to Python 2:
> 
> ```bash
> sudo ln -s /usr/bin/python2 /usr/bin/python
> ```

---

## Cloning the Repository

Clone the repository from GitHub:

```bash
git clone https://github.com/anubhavg-icpl/wmiclient.git
```

Then change into the cloned directory:

```bash
cd wmiclient
```

---

## Setting Up the Source Files

Navigate to the `Samba/source` directory and set the necessary execute permissions:

```bash
cd Samba/source
chmod +x *.sh
chmod +x ./configure
chmod +x heimdal_build/*.sh
chmod +x script/*.sh
```

Then return to the root of the repository:

```bash
cd ../..
```

---

## Building wmiclient

Before building, set the environment variable `ZENHOME` to `/usr`:

```bash
export ZENHOME=/usr
```

Now, run the build command:

```bash
make "CPP=gcc -E -ffreestanding"
```

If the build completes successfully, the `wmic` binary will be generated in `Samba/source/bin/`.

---

## Installing wmiclient

Copy the generated binary to `/bin` so it’s available system-wide:

```bash
sudo cp Samba/source/bin/wmic /bin
```

---

## Testing the Installation

You can test the installation by running:

```bash
wmic --help
```

This should display the help output for `wmic`.

---

## Troubleshooting

- **Missing Python Error:**  
  If you encounter an error such as:
  ```
  Missing: PYTHON               /usr/bin/python
  ```
  Ensure that Python is installed and available at `/usr/bin/python`. Creating a symbolic link from `/usr/bin/python2` to `/usr/bin/python` (as shown above) should resolve this issue.

- **Warnings about Man Pages:**  
  The warnings from `update-alternatives` about skipping the creation of man pages (for `rsh`, `rlogin`, `rcp`) are harmless and can be safely ignored.
