#!/usr/bin/env bash

set -euo pipefail

: "${PDF_PASSWORD:?Set PDF_PASSWORD without committing it}"

source_dir="${1:-tmp/pdfs/source}"
output_dir="${2:-assets/lectures}"

render_deck() {
  week="$1"
  filename="$2"
  destination="$output_dir/week-$week"

  mkdir -p "$destination"
  pdftoppm \
    -upw "$PDF_PASSWORD" \
    -jpeg \
    -scale-to-x 1600 \
    -scale-to-y -1 \
    -jpegopt quality=88,progressive=y,optimize=y \
    "$source_dir/$filename" \
    "$destination/slide"

  for rendered in "$destination"/slide-0?.jpg; do
    [ -e "$rendered" ] || continue
    base="$(basename "$rendered")"
    mv "$rendered" "$destination/${base/slide-0/slide-}"
  done
}

render_deck 01 lecture1_intro.pdf
render_deck 02 lecture2_control_mdp.pdf
render_deck 03 lecture3_imitation.pdf
render_deck 04 lecture4_rl_I.pdf
render_deck 05 lecture5_rl_II.pdf
render_deck 06 lecture6_generative.pdf
render_deck 07 lecture7_sequence_modeling.pdf
render_deck 08 lecture8_world_models.pdf
render_deck 09 lecture9_generalist_policies.pdf
render_deck 10 lecture10_reasoning.pdf
render_deck 11 lecture11_frontiers.pdf

printf 'Rendered %s slide images.\n' "$(find "$output_dir" -name 'slide-*.jpg' | wc -l | tr -d ' ')"
