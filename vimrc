" :se[t] all&		Set all options, except terminal options, to their
"			default value.  The values of 'term', 'lines' and
"			'columns' are not changed. {not in Vi}
"%s/import( \"stringUtils\/1\/stringUtil.ggl\" )/import( \"gglUtils\/\".. os.getenv( \'GGLUTILS_VERSION\' ) ..\"/stringUtils.ggl\" )/g 
set all&

filetype plugin on
" sexy indent plug
filetype plugin indent on

set ofu=syntaxcomplete#Complete

" Taglist variables
" Display function name in status bar:
"let g:ctags_statusline=1
" Automatically start script
let generate_tags=1
" Displays taglist results in a vertical window:
let Tlist_Use_Horiz_Window=0
" Shorter commands to toggle Taglist display
nnoremap TT :TlistToggle<CR>
map <F4> :TlistToggle<CR>
map :W :w
map :E :e
map :Q :q
map :Vs :vs

" Various Taglist diplay config:
let Tlist_Use_Right_Window = 1
let Tlist_Compact_Format = 1
let Tlist_Exit_OnlyWindow = 1
let Tlist_GainFocus_On_ToggleOpen = 1
let Tlist_File_Fold_Auto_Close = 1

" Dictionnary Word Completion using Ctrl-x Ctrl-k
set dictionary+=/usr/share/dict/words

" python tab feature:
" filetype plugin on
let g:pydiction_location = '/usr/people/jordi-r/.vim/after/ftplugin/pydiction-1.2/complete-dict'

" Try to preserve the expand mode of the original file.
" Highlight mismatches as bad
highlight BadWhitespace ctermbg=red guibg=red
"fu Select_tab_style()
    "if search('^    ', 'n', 10)
		"" Display tabs at the beginning of a line in Python mode as bad.
		"" Expand tabs into spaces
        "set expandtab
		"match BadWhitespace /^\t\+/
		"redraw | echo "Whitespace is SPACES"
    "el 
		"" Display spaces at the beginning of a line in Python mode as bad.
		"" Don't expand tabs into spaces
        "set noexpandtab
		"match BadWhitespace /^ \+/
		"redraw | echo "Whitespace is TABS"
    "en
"endf
"au BufRead,BufNewFile *.py,*.pyw call Select_tab_style()

" Tabs/spaces
set tabstop=4
set shiftwidth=4
set softtabstop=4

set autochdir
set nonumber
set nu!
set wrapscan
set guifont=-misc-fixed-medium-r-normal--18-120-100-100-c-90-iso8859-1
set hlsearch
set incsearch
set ruler
set menuitems=100
set backspace=indent,eol,start
set smartindent

":map <C-t> :tabnew<cr>
":map <C-w> :tabclose<cr>


syntax on
autocmd BufEnter *.ggl set filetype=lua
autocmd BufEnter *.html.twig set filetype=twig

" compatible	behave very Vi compatible (not advisable)
set nocp

" whichwrap	list of flags specifying which commands wrap to another line
"	(local to window)
set ww=

" ignorecase	ignore case when using a search pattern
"set ic

" smartcase	override 'ignorecase' when pattern has upper case characters
"set scs

" linebreak	wrap long lines at a character in 'breakat'
"	(local to window)
set lbr

" columns	width of the display
set co=99

" lines	number of lines in the display
" set lines=80

" list	show <Tab> as ^I and end-of-line as $
"	(local to window)
" set list

" listchars	list of strings used for list mode
" set lcs=tab:→·,trail:_,nbsp:␣

" background	"dark" or "light"; the background color brightness
"set bg=dark

" hlsearch	highlight all matches for the last used search pattern
set hls

" spell	highlight spelling mistakes
"	(local to window)
"set spell

" hidden	don't unload a buffer when no longer shown in a window
set hid

" tabpagemax	maximum number of tab pages to open for -p and "tab all"
set tpm=100

" scrolljump	minimal number of lines to scroll at a time
set sj=-25

" guifont	list of font names to be used in the GUI
 "set gfn=Fixed18,

" visualbell	use a visual bell instead of beeping
set vb

" showcmd	show (partial) command keys in the status line
set sc

" textwidth	line length above which to break a line
"	(local to buffer)
set tw=99

" backspace	specifies what <BS>, CTRL-W, etc. can do in Insert mode
set bs=indent,start

" formatoptions	list of flags that tell how automatic formatting works
"	(local to buffer)
"set fo=tcrq
set fo=crq

" completeopt	whether to use a popup menu for Insert mode completion
set cot=menu,longest,preview


"
" shiftwidth	number of spaces used for each step of (auto)indent
"	(local to buffer)
"set sw=4

" softtabstop	if non-zero, number of spaces to insert for a <Tab>
"	(local to buffer)
"set sts=4

" shiftround	round to 'shiftwidth' for "<<" and ">>"
set sr

" expandtab	expand <Tab> to spaces in Insert mode
"	(local to buffer)
set et

" fileformats	list of file formats to look for when editing a file
set ffs=unix,dos,mac

" directory	list of directories for the swap file
set dir=~/tmp/vim.swp//,~/tmp//,/var/tmp//,/tmp//,.

" history	how many command lines are remembered 
set hi=1000

" virtualedit	when to use virtual editing: "block", "insert" and/or "all"
set ve=block

hi Normal guibg=Black guifg=LightGray

" Set the colors
"colorscheme liquidarbon
colorscheme darkblue

au BufRead,BufNewFile set filetype=python
autocmd BufEnter *.html set filetype=htmldjango

if getline(1) =~ '-*-c++-*-'
    set filetype=cpp
endif

" remapping
inoremap <Tab> <C-R>=SmartTab(1)<CR>
inoremap <S-Tab> <C-R>=SmartTab(0)<CR>

map o o<ESC>
map O O<ESC>
map <C-S> :w<CR>
map <D-5> :%s/\s*$//g<CR>:noh<CR>
map <D-4> :%s/\t/    /g<CR>:noh<CR>
"map <D-4> :%s/    /\t/g<CR>:noh<CR>

map <F10> Iimport pdb; pdb.set_trace()<CR><ESC>
map <F11> :tabprevious<CR>:set co=161<CR>:vsplit<CR>:bn<CR>:tabnext<CR>:q<CR>

" quicker window navigation
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-h> <C-w>h
nnoremap <C-l> <C-w>l

" quicker buffer navigation
nnoremap <C-n> :next<CR>
nnoremap <C-p> :prev<CR>

" Set the default file encoding to UTF-8: 
set encoding=utf-8

" Content awareness
let python_highlight_all=1

" Bind ctrl + space for completion
:imap <C-Space> <C-X><C-O>

" Alert when we get too long
"highlight WarnLength ctermbg=darkred ctermfg=white guibg=#773333
"match WarnLength /\%>99v.\+/
set cc=99

" Keep a couple of context lines
set scrolloff=2

" Warn about any trailing whitespace
au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/
" Makefiles don't want tab expansion, it really breaks it.
au BufRead,BufNewFile Makefile* set noexpandtab

" Window Furniture
set ruler
set visualbell

" Folding
set foldlevelstart=0
set foldmethod=indent
nnoremap <Space> za
vnoremap <Space> za

" Vim's Awsome Undo Exposed with gundo
nnoremap ` :GundoToggle<CR>
let g:gundo_width = 60
let g:gundo_preview_height = 40
let g:gundo_right = 0


" CtrlP config
set runtimepath^=~/.vim/bundle/ctrlp.vim
set wildignore+=*/tmp/*,*.so,*.swp,*.zip     " MacOSX/Linux
let g:ctrlp_custom_ignore = {
  \ 'dir':  '\.git$\|\.hg$\|\.svn$\|\.yardoc\|data\|logs\|cache\|vendor\|tmp$',
  \ 'file': '\.exe$\|\.so$\|\.dat$'
  \ }
let g:ctrlp_map = '<c-p>'
let g:ctrlp_cmd = 'CtrlP'

""You need the next line to change the color back when you hit escape.
"inoremap <Esc> <Esc>:colorscheme liquidcarbon<cr>
"colorscheme liquidcarbon


