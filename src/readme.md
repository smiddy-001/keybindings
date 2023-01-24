## keybinding Globalisation Project

**Application**' & '**OS**' **keybinds** that cross-integrate **_seamlessley_**.

### The Problem

I am just starting in linux and noticing a shitload more keybinds I need to remember
and most of em can and should be different.
I believe a global keybind list for all tasks and actions (2d/3d editing, file management, window management, tab switching, movie editing) to be in unity with one-another.

---

### Inspiration

I took a liking to vim and its excelently orchestrated keybinds especially the hjkl and the consideration to where your fingers should be placed for minimal distance between common keys and ergonomics when two handed typing which meant those who are familiar with the keybinds speed through files and code faster than ever possible with an ordinary IDE.

![heatmap of most common keyboard keys]('https://cdn.arstechnica.net/wp-content/uploads/2014/03/dvorak3.jpg')

---

### The Solution

I will be taking alot from what I have learnt from vim's way of keybindings and applying them to a big big list of keybinds for my OS and config files for common apps and possibly a multilingual (code multilingual) config file for personal use in my future applications and projects.

I also believe alot is to be learnt from the gaming industry as they have the creative leeway to require more or unusual tasks from their keybindings hence good games really need to be smart about what key does what and probably spend the most time thinking and planning their keybinds of all software.

---

file structure of this project

```
keybindings
│   README.md               -actual readme (with big keybind list)
│   main.py                 -sets up README.md
│   launch.sh               -a uber simple bash script that runs py
│   LICENSE                 -the liscence
│
└───src
│   │   logs.txt            -logs the output when the py file is run
│   │   readme.md           -minimal readme (no keybinds)
│   │
│   └───keybinds
│       │   default.csv     -default keybinding list
│       │   2dpaintapp.csv  -2dpaintapp keybinding list
│       │   ...             -the keybinding list keeps going
```

---

### Every Single Type Of Software Ever <sup>(easier said than done)</sup>

Some apps may need to be split up into their managable components, like video editing and audio editing although they may ship with the same software. With the intent being I have to change this repo as little as humanly possible and that there is an end to this project where everything will be satisfied.

#### **General Stuff / Web**

| id  | type of service | example app |
| :-- | :-------------- | :---------- |
| wbr | web browser     | firefox     |
| gen | general         | OS          |

#### **Visuals & Animation**

| id  | type of service    | example app |
| :-- | :----------------- | :---------- |
| tde | 2d editors         | photoshop   |
| tds | 2d sketch programs | sketchup    |
| tre | 3d editors         | blender     |
| tdr | 3d rendering       | xrender     |
| scr | screen recording   | obs-studio  |

#### **Word Prosessing**

| id  | type of service  | example app    |
| :-- | :--------------- | :------------- |
| txe | text editor      | notepad        |
| rte | rich text editor | microsoft word |

#### **Presentations**

| id  | type of service          | example app       |
| :-- | :----------------------- | :---------------- |
| psi | presentations (simple)   | LaTex             |
| pad | presentations (advanced) | microsoft present |

#### **Spreadsheets**

| id  | type of service     | example app     |
| :-- | :------------------ | :-------------- |
| sse | spreadsheet editor  | microsoft excel |
| dbm | database management | idfk...         |

#### **Financial Management**

| id  | type of service      | example app |
| :-- | :------------------- | :---------- |
| fim | financial management | xero        |

#### **Games**

| id  | type of service      | example app |
| :-- | :------------------- | :---------- |
| fim | financial management | xero        |

one quick thing before I start spamming keybinds and that. Below is how emacs shortens their keybinds and it is shorter to write. deal with it

```
C : ctr key
M : Meta Key win key
A : alt key
S : space key
C-shift : ctr + shift key

C-f-c = CTRL + f + c
C-F-c = CTRL + F + c
M-q   = META + q
```

<div id="big-list-of-keybindings"></div>
