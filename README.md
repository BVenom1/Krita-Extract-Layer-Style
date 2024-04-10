# Krita-Extract-Layer-Style

Krita extention to extract the layer style of a paint layer to its own layer

## Installation

To download the plugin, download the .zip file from [releases](https://github.com/BVenom1/Krita-Extract-Layer-Style/releases). You can place this file in any appropriate location. Ideally create a folder in `~/.local/share/krita` for Linux or `C:\Users\username\AppData\Roaming\krita` for Windows for the purpose of storing downloaded plugins.

Then open Krita, on the Main-Menu bar go to Tools > Scripts > Import Python Plugin from File..., navigate to the plugin in the file explorer popup and select it. This will install the plugin to Krita.

## Usage

1. Open a document in Krita.
2. select a layer with a layer style (or without, in which case the result will be an empty paint layer).
3. go to Tools > Scripts > Extract Layer Style.

## Caveats

- This action consumes 5 steps in krita, so to undo it, you will have to press Ctrl+Z 5 times.
- if there are multiple layer styles on the selected layer, they will all be extracted into a single layer.
