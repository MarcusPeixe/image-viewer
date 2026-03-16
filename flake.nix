{
  description = "Simple Python Development Environment";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs { inherit system; };
        python = pkgs.python312.withPackages (
          ps: with ps; [
            virtualenv
          ]
        );
      in
      {
        devShells.default = pkgs.mkShell {
          packages = [ python ];
        };

        packages.default = pkgs.writeShellApplication {
          name = "image-viewer";
          runtimeInputs = [ python ];
          text = ''
            PROJECT_DIR="/Users/markids/Programs/python/image-viewer"

            exec "$PROJECT_DIR/bin/python3.12" "$PROJECT_DIR/image.py" "$@"
          '';
        };

        apps.default = {
          type = "app";
          program = "${self.packages.${system}.default}/bin/image-viewer";
        };
      }
    );
}
