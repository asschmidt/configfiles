local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
  vim.fn.system({
    "git",
    "clone",
    "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    "--branch=stable", -- latest stable release
    lazypath,
  })
end
vim.opt.rtp:prepend(lazypath)

local plugins = {
  'wbthomason/packer.nvim',
  'ellisonleao/gruvbox.nvim',
  'rebelot/kanagawa.nvim',
  {
    'dracula/vim',
    lazy = false,
  },
  'nvim-tree/nvim-tree.lua',
--  'nvim-treesitter/nvim-treesitter',
--  'nvim-tree/nvim-web-devicons',
  'nvim-lualine/lualine.nvim',
  'bluz71/vim-nightfly-colors',
  'vim-test/vim-test',
  'lewis6991/gitsigns.nvim',
  'preservim/vimux',
  'christoomey/vim-tmux-navigator',
  'tpope/vim-fugitive',
  'tpope/vim-commentary',
  'mbbill/undotree',

  {
	  'nvim-telescope/telescope.nvim',
	  tag = '0.1.0',
	  dependencies = { {'nvim-lua/plenary.nvim'} }
  },

  'VonHeikemen/lsp-zero.nvim',
   -- LSP Support
  'neovim/nvim-lspconfig',
  'williamboman/mason.nvim',
  'williamboman/mason-lspconfig.nvim',

  -- Autocompletion
  'hrsh7th/nvim-cmp',
  'hrsh7th/cmp-buffer',
  'hrsh7th/cmp-path',
  'saadparwaiz1/cmp_luasnip',
  'hrsh7th/cmp-nvim-lsp',
  'hrsh7th/cmp-nvim-lua',

  -- Snippets
  'L3MON4D3/LuaSnip',
  'rafamadriz/friendly-snippets',

  -- completion
--  'hrsh7th/nvim-cmp',
--  'hrsh7th/cmp-nvim-lsp',
--  'L3MON4D3/LuaSnip',
--  'saadparwaiz1/cmp_luasnip',
--  "rafamadriz/friendly-snippets",
--  "github/copilot.vim",
--  "williamboman/mason.nvim",
--  "neovim/nvim-lspconfig",
--  "williamboman/mason-lspconfig.nvim",
--  "glepnir/lspsaga.nvim",
--  {
--	  'nvim-telescope/telescope.nvim',
--	  tag = '0.1.0',
--	  dependencies = { {'nvim-lua/plenary.nvim'} }
-- }
}

local opts = {}

--require("lazy").setup({{"nvim-treesitter/nvim-treesitter", build = ":TSUpdate"}})
require("lazy").setup(plugins, opts)
