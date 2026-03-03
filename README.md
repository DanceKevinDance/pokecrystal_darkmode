# Pokémon Crystal - Dark Mode

This is a fork of the [pokecrystal](https://github.com/pret/pokecrystal) project aimed at adding accessibility to the game in the form of a dark mode style theme. It isn't perfect, there are compromises, but for people with low vision like myself, it's the only way some of us can play these older games. 

## How to Play

### Build it Yourself
1. Clone this repo
2. Follow the steps in the base [pokecrystal](https://github.com/pret/pokecrystal) repo install guide or the install file in this repo - they're the same

### Use the Patch File
1. Download the .bps patch from the latest release of this repo
2. Download [FLIPS](https://www.romhacking.net/utilities/1040/)
3. Run FLIPS and select this hack's patch
4. Select your base ROM (I used the US/EU version to make the patch)

### If you're a ROM hacker and would like to make a dark mode version of your hack, find the .zip file in the latest release

## Featues

- All or most menus and GUIs in the game have been given black backgrounds with white text
- Pokémon and trainers have had their sprites' backgrounds turned black so they're not big white boxes on a black background
- Lots of small menu elements have been inverted to match the dark mode theme, though there are ikely some missed or that need editing

## Compromises/Known Issues

- To make the Pokémon front pics render right in battle, I had to upscale all of them to fill the 7x7 square the engine draws. If you're familiar with this game/engine and would like to try and help me work around the issue, please reach out
- Some things are just always going to be a little odd. Removing the background from the sprites can be a little scuffed. Some moves or animations are going to look a little funny. If something looks really bad or isn't dark like it should be, feel free to report it.
- Substitution and minimize are both weird looking

## Notes

- I've left the default readme from pokecrystal master below to make sure all the information there is easy to access.
- I am not a programmer or artist. I'm just doing my best to figure all this out as I go. This is my first ROM hack, my first GitHub repo, etc, so if something is wrong or weird or whatever, please bare with me.
- As mentioned, this is a project focused on accessibility and making the game playable for a subset of people. I'd love anyone who's interested to be able to play it, and I think it came out pretty good, but that is the focus.
- I cannot make a less high-contrast version (e.g. dark grey instead of black) because of the way palettes are defined in the game and the fact they're limited to 4 colors, two of those being locked to black and white. The backgrounds could be grey, but then the sprites would have either black or white boxes. 

@@ My Other Projects

[Pokémon Crystal Dark Mode](https://github.com/DanceKevinDance/pokecrystal_darkmode)
	[Pokémon Super Crystal - Dark Mode](https://github.com/DanceKevinDance/Pokemon_Super_Crystal_DarkMode/releases/tag/release)

[The Elder Scrolls IV: Oblivion Remastered - Dark Mode UI](https://www.nexusmods.com/oblivionremastered/mods/3317?tab=description)


# Pokémon Crystal [![Build Status][ci-badge]][ci]

This is a disassembly of Pokémon Crystal.

It builds the following ROMs:

- Pokemon - Crystal Version (UE) (V1.0) [C][!].gbc `sha1: f4cd194bdee0d04ca4eac29e09b8e4e9d818c133`
- Pokemon - Crystal Version (UE) (V1.1) [C][!].gbc `sha1: f2f52230b536214ef7c9924f483392993e226cfb`
- Pokemon - Crystal Version (A) [C][!].gbc `sha1: a0fc810f1d4e124434f7be2c989ab5b5892ddf36`
- CRYSTAL_ps3_010328d.bin `sha1: c60d57a24bbe8ecf7cba54ab3f90669f97bd330d`
- CRYSTAL_ps3_us_revise_010710d.bin `sha1: 391ae86b1d5a26db712ffe6c28bbf2a1f804c3c4`
- CGBBYTE1.784.patch `sha1: a25517f60ca0e887d39ec698aa56a0040532a4b3`

To set up the repository, see [INSTALL.md](INSTALL.md).


## See also

- [**FAQ**](FAQ.md)
- [**Documentation**][docs]
- [**Wiki**][wiki] (includes [tutorials][tutorials])
- [**Symbols**][symbols]
- [**Tools**][tools]

You can find us on [Discord (pret, #pokecrystal)](https://discord.gg/d5dubZ3).

For other pret projects, see [pret.github.io](https://pret.github.io/).

[docs]: https://pret.github.io/pokecrystal/
[wiki]: https://github.com/pret/pokecrystal/wiki
[tutorials]: https://github.com/pret/pokecrystal/wiki/Tutorials
[symbols]: https://github.com/pret/pokecrystal/tree/symbols
[tools]: https://github.com/pret/gb-asm-tools
[ci]: https://github.com/pret/pokecrystal/actions
[ci-badge]: https://github.com/pret/pokecrystal/actions/workflows/main.yml/badge.svg
