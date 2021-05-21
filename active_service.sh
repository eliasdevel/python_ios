#!/bin/bash

echo "[Unit]" > /etc/systemd/system/io_register_service.service
echo "Description=IO service" >> /etc/systemd/system/io_register_service.service
echo "Wants=network.target" >> /etc/systemd/system/io_register_service.service
echo "After=network.target" >> /etc/systemd/system/io_register_service.service
echo "[Service]" >> /etc/systemd/system/io_register_service.service
echo "Type=simple" >> /etc/systemd/system/io_register_service.service
echo "Restart=always" >> /etc/systemd/system/io_register_service.service
echo "RestartSec=3" >> /etc/systemd/system/io_register_service.service
echo "User=pi" >> /etc/systemd/system/io_register_service.service
echo "ExecStart=/usr/bin/env python /home/pi/python_ios/io_service.py" >> /etc/systemd/system/io_register_service.service
echo "[Install]" >> /etc/systemd/system/io_register_service.service
echo "WantedBy=multi-user.target" >> /etc/systemd/system/io_register_service.service


sudo systemctl disable io_register_service.service

sudo systemctl enable io_register_service.service

sudo systemctl status io_register_service.service