import logging.config
import os
from datetime import datetime
from pathlib import Path

from fastapi import FastAPI

from app import app_base_path
from app.exception.exception_handler import ExceptionHandler
from app.router import routers_base_path
from app.util.config_manager import ConfigManager
from app.util.import_util import ImportUtil

app = FastAPI()
ConfigManager.initiate_config()
ExceptionHandler.initiate_exception_handlers(app)

# add routers
__router_modules = ImportUtil.import_modules_from_directory_as_list(routers_base_path)
for router_module in __router_modules:
    app.include_router(router_module.router, prefix=router_module.prefix)

# initiate logging
logging_folder = ConfigManager.get_specific_config(section="logging", key="folder")

Path(os.path.join(os.path.dirname(app_base_path), logging_folder)).mkdir(exist_ok=True)

logging_config_file_path = os.path.join(os.path.dirname(app_base_path), 'logging.ini')
logging.config.fileConfig(logging_config_file_path,
                          defaults={'date': datetime.now().strftime('%Y-%m-%d-%H-%M-%S')},
                          # specifies value for %(date)s in logging.ini file
                          disable_existing_loggers=False)
