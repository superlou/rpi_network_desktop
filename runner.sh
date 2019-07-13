until `python3 main.py`; do
	echo "RPi network desktop crashed with exit code $?. Respawning..." >&2
	sleep 1
done
