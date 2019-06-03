#!/bin/bash

groupadd cr0n0s
useradd -d /home/flag_cr0n0s -G cr0n0s -m -U -s /bin/bash flag_cr0n0s
useradd -d /home/user_cr0n0s -G cr0n0s -m -U -s /bin/bash user_cr0n0s
chmod go-x /home/*_cr0n0s

echo "user_cr0n0s:wannacron" | chpasswd

mkdir /home/scripts
chown flag_cr0n0s:cr0n0s /home/scripts
chmod 777 /home/scripts
echo "umask 0006" >> /home/user_cr0n0s/.bashrc
cat > /home/run_scripts.sh <<'EOF'
#!/bin/bash

for ((i=0; i<7; i++))
do
counter=0
declare -a users
for script in /home/scripts/*
do
username=$(stat --format '%U' $script)
if [[ ${users[$username]} ]]
then
echo "no"
else
users=( "${users[*]}" "$username" )
timeout 5 $script
fi
done
sleep 8
unset users
done
EOF

chown flag_cr0n0s:flag_cr0n0s /home/run_scripts.sh
chmod 755 /home/run_scripts.sh
echo "* * * * * flag_cr0n0s /home/run_scripts.sh" >> /etc/crontab
echo flag{i_kn0w_cr0n_4nd_1ik3_17} > /home/flag_cr0n0s/flag.txt

mkdir /var/run/sshd
sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
