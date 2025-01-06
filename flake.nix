# SPDX-License-Identifier: GPL-2.0-or-later

{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };
  outputs = {self, nixpkgs, flake-utils}:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
        };
      in {
        packages.default = pkgs.python313Packages.buildPythonPackage rec {
          pname = "teestream";
          version = "0.1.0";
          src = ./.;
          doCheck = false;
          pyproject = true;
          nativeBuildInputs = with pkgs.python313Packages; [
            hatchling
          ];
        };
      }
    );
}
