import subprocess
import asyncio
import os
import sys


HOMEBREW_PATH = '/home/gamer/homebrew'
# from config import logging
import config
from gpu import gpuManager
from cpu import cpuManager
from fan import fanManager
from sysInfo import sysInfoManager

import decky_plugin

logging = decky_plugin.logging

logging.info("PowerControl main.py")


class Plugin:
    async def _main(self):
        while True:
            await asyncio.sleep(3)

    async def get_hasRyzenadj(self):
        try:
            return cpuManager.get_hasRyzenadj()
        except Exception as e:
            logging.error(e)
            return False

    async def get_cpuMaxNum(self):
        try:
            return cpuManager.get_cpuMaxNum()
        except Exception as e:
            logging.error(e)
            return 0

    async def get_tdpMax(self):
        try:
            return cpuManager.get_tdpMax()
        except Exception as e:
            logging.error(e)
            return 0
    
    async def get_gpuFreqMax(self):
        try:
            return gpuManager.get_gpuFreqMax()
        except Exception as e:
            logging.error(e)
            return 0
    
    async def get_gpuFreqMin(self):
        try:
            return gpuManager.get_gpuFreqMin()
        except Exception as e:
            logging.error(e)
            return 0
    
    async def get_gpuFreqMin(self):
        try:
            return gpuManager.get_gpuFreqMin()
        except Exception as e:
            logging.error(e)
            return 0

    async def get_cpu_AvailableFreq(self):
        try:
            return cpuManager.get_cpu_AvailableFreq()
        except Exception as e:
            logging.error(e)
            return []
    async def get_language(self):
        try:
            return sysInfoManager.get_language()
        except Exception as e:
            logging.error(e)
            return ""

    async def get_fanRPM(self):
        try:
            return fanManager.get_fanRPM()
        except Exception as e:
            logging.error(e)
            return 0
    
    async def get_fanRPMPercent(self):
        try:
            return fanManager.get_fanRPMPercent()
        except Exception as e:
            logging.error(e)
            return 0
    
    async def get_fanTemp(self):
        try:
            gpuTemp = sysInfoManager.get_gpuTemp()
            if gpuTemp!=-1:
                return gpuTemp
            return sysInfoManager.get_cpuTemp()
        except Exception as e:
            logging.error(e)
            return 0
    
    async def get_fanIsAuto(self):
        try:
            return fanManager.get_fanIsAuto()
        except Exception as e:
            logging.error(e)
            return 0
    
    async def get_fanMAXRPM(self):
        try:
            return fanManager.get_fanMAXRPM()
        except Exception as e:
            logging.error(e)
            return 0
    
    async def get_fanIsAdapted(self):
        try:
            return fanManager.get_fanIsAdapted()
        except Exception as e:
            logging.error(e)
            return 0
    
    def set_fanAuto(self, value:bool):
        try:
            return fanManager.set_fanAuto(value)       
        except Exception as e:
            logging.error(e)
            return False

    def set_fanPercent(self, value:int):
        try:
            return fanManager.set_fanPercent(value)         
        except Exception as e:
            logging.error(e)
            return False

    def set_gpuAuto(self, value:bool):
        try:
            return gpuManager.set_gpuAuto(value)        
        except Exception as e:
            logging.error(e)
            return False

    def set_gpuAutoMaxFreq(self, value: int):
        try:
            return gpuManager.set_gpuAutoMaxFreq(value)
        except Exception as e:
            logging.error(e)
            return False
    
    def set_gpuAutoMinFreq(self, value: int):
        try:
            return gpuManager.set_gpuAutoMinFreq(value)
        except Exception as e:
            logging.error(e)
            return False

    def set_gpuFreq(self, value: int):
        try:
            return gpuManager.set_gpuFreq(value)
        except Exception as e:
            logging.error(e)
            return False
    
    def set_gpuFreqRange(self, value: int, value2: int):
        try:
            return gpuManager.set_gpuFreqRange(value,value2)
        except Exception as e:
            logging.error(e)
            return False

    def set_cpuTDP(self, value: int):
        try:
            return cpuManager.set_cpuTDP(value)
        except Exception as e:
            logging.error(e)
            return False

    def set_cpuOnline(self, value: int):
        try:
            return cpuManager.set_cpuOnline(value)
        except Exception as e:
            logging.error(e)
            return False

    def set_smt(self, value: bool):
        try:
            return cpuManager.set_smt(value)
        except Exception as e:
            logging.error(e)
            return False
    
    def set_cpuBoost(self, value: bool):
        try:
            return cpuManager.set_cpuBoost(value)
        except Exception as e:
            logging.error(e)
            return False

    def set_cpuFreq(self, value: int):
        try:
            return cpuManager.set_cpuFreq(value)
        except Exception as e:
            logging.error(e)
            return False
    
    def receive_suspendEvent(self):
        try:
            return True
        except Exception as e:
            logging.error(e)
            return False
