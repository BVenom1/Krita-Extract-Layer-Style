# BVenom's Extract Layer Style Extension for Krita

Krita extension to extract the layer style of a paint layer to its own layer.

The actual technique is the same as TheTwo's for extracting a layer style, which they outlined [here](https://krita-artists.org/t/some-methods-of-simulating-photoshop-functions/27819).

## Installation

To download the plugin, download the .zip file from [releases](https://github.com/BVenom1/Krita-Extract-Layer-Style/releases). You can place this file in any appropriate location. Ideally create a folder in `~/.local/share/krita` for Linux or `C:\Users\username\AppData\Roaming\krita` for Windows for the purpose of storing downloaded plugins.

Then open Krita, on the Main-Menu bar go to Tools > Scripts > Import Python Plugin from File..., navigate to the plugin in the file explorer popup and select it. This will install the plugin to Krita.

## Usage

1. Open a document in Krita.
2. select a layer with a layer style (or without, in which case the result will be an empty paint layer).
3. go to `Tools > Scripts` and click `Extract Layer Style`.

## OK but what is it actually doing?

when the `Extract Layer Style` button is pressed:
1. The current layer is copied.
2. The copy is placed in a group.
3. The blend mode of the copy is set to `Erase` (Which makes the contents of the layer invisible, while preserving the layer style, as it is not affected by the blending mode of the layer itself).
4. A vector layer is created above the group.
5. The vector layer is merged down, which merges the group also, giving a paint layer with just the contents of the layer style.

The reason I had to go through such a round-about method for merging the group was because I couldn't find an action that would merge the group in one step. If I find that function, then the process will only have 4 steps instead of 5.

## Caveats

- This action consumes 5 steps in krita, so to undo it, you will have to press Ctrl+Z 5 times.
- if there are multiple layer styles on the selected layer, they will all be extracted into a single layer.
