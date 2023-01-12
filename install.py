import launch

if not launch.is_installed("transparent-background"):
    launch.run_pip("install transparent-background", "requirements for Ebsynth Utility")

if not launch.is_installed("ipython"):
    launch.run_pip("install ipython", "requirements for Ebsynth Utility")

if not launch.is_installed("seaborn"):
    launch.run_pip("install ""seaborn>=0.11.0""", "requirements for Ebsynth Utility")

