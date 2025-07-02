{
  description = "Flake to manage python workspace";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/08f22084e6085d19bcfb4be30d1ca76ec";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        python = pkgs.python313;
        python_packages = python.withPackages(ps: with ps;[
          pytelegrambotapi
          telethon
          requests
          python-dotenv
        ]);
      in {
        devShells.default = pkgs.mkShell {
          buildInputs = [
            python_packages
          ];
        };
      });
}
