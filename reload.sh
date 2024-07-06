 #!/bin/bash

pnpm run build
sudo rm -r /home/$USER/homebrew/plugins/FanControl/
sudo cp -r /home/$USER/Development/FanControl/ ~/homebrew/plugins/
sudo systemctl restart plugin_loader.service
