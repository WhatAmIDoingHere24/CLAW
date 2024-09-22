#!/bin/bash

# check for gum, if its in this dir, make this dir part of path
if [[ -e ./gum ]]; then
    export PATH=$PATH:$(pwd)
else
    echo "Put a gum executable in this directory"
    exit 1
fi

# Ideas:
# Users have passwords, names, login shell, home dir, whether they can login, and admin status; these properties should be editable
# Groups have permissions and the users in them; these should be editable
# Script should be able to add/delete users
# Script should be able to add/delete groups

# adds a specified user to a group
# accomplishes the same thing as addUserToGroup, but in reverse
# $1 = user name
addGroupToUser(){
    # render group list table, hold the chosen line in GROUPTABLECHOICE
    # don't touch the separator, its & because it cant be space or ,
    GROUPTABLECHOICE="$(sudo cat /etc/group \
    | column -s ":" -t -N "Group Name,Password,GID,Users" \
    | gum table --separator="&" --height=8 --widths=120)"

    #filter the chosen line to be just the group name
    CHOSENGROUPNAME="$(echo "$GROUPTABLECHOICE"\
    | awk '{print $1}'\
    | tr -d ' ')"

    if [[ $CHOSENGROUPNAME == "" ]]; then
        echo "No group was specified"
        return
    fi

    sudo usermod -aG "$CHOSENGROUPNAME" "$1"
    echo "Added user $1 to group $CHOSENGROUPNAME"
}

# removes a specified user from a group
# accomplishes the same thing as removeUserFromGroup, but in reverse
# $1 = user name
removeGroupFromUser(){
    # render group list table, hold the chosen line in GROUPTABLECHOICE
    # don't touch the separator, its & because it cant be space or ,
    GROUPTABLECHOICE="$(sudo cat /etc/group \
    | column -s ":" -t -N "Group Name,Password,GID,Users" \
    | gum table --separator="&" --height=8 --widths=120)"

    #filter the chosen line to be just the group name
    CHOSENGROUPNAME="$(echo "$GROUPTABLECHOICE"\
    | awk '{print $1}'\
    | tr -d ' ')"

    if [[ $CHOSENGROUPNAME == "" ]]; then
        echo "No group was specified"
        return
    fi

    sudo usermod -rG "$CHOSENGROUPNAME" "$1"
    echo "Removed user $1 from group $CHOSENGROUPNAME"
}

# takes input for a new shell path, and changes it for the specified user
# $1 = user's name
changeUserShell(){
    CHOSENSHELLPATH=$(gum input --header="Enter the new shell's path:" \
    --header.foreground="255" \
    --placeholder="Example: /usr/bin/bash" \
    )

    if [[ "$CHOSENSHELLPATH" == "" ]]; then
        echo "No path was specified"
        return
    elif [[ ! -e $CHOSENSHELLPATH ]]; then
        echo "That shell doesn't exist"
        return
    fi

    sudo usermod -s "$CHOSENSHELLPATH" "$1"
    echo "Changed user $1's shell to $CHOSENSHELLPATH"
}

# changes the specified user's home directory to what is typed in
# $1 = user's name
changeUserHomeDirectory(){
    CHOSENDIRPATH=$(gum input --header="Enter the new home directory:" \
    --header.foreground="255" \
    --placeholder="Example: /home/<user's name>" \
    )

    if [[ "$CHOSENDIRPATH" == "" ]]; then
        echo "No path was specified"
        return
    elif [[ ! -d $CHOSENDIRPATH ]]; then
        echo "That directory does not exist"
        return
    fi

    sudo usermod -d "$CHOSENDIRPATH" "$1"
    echo "Set user $1's home dir to $CHOSENDIRPATH"
}

# function for editing the users, called from main menu
# < no parameters >
editUsers(){
    #render user list table, hold the chosen line in USERTABLECHOICE
    USERTABLECHOICE="$(sudo cat /etc/passwd\
    | column -s ":" -t -N "Name,Password,UID,GID,Comments,Home Directory,Login Shell"\
    | gum table --height=8 --widths=120)"

    #filter the chosen line to be just the username
    CHOSENUSERNAME="$(echo "$USERTABLECHOICE"\
    | awk '{print $1}'\
    | tr -d ' ')"

    if [[ $CHOSENUSERNAME == "" ]]; then
        echo "No user was specified"
        return
    fi

    #choice of what action to do for the chosen user
    USERCHOICE="$(gum choose \
    --header="Editing user: $(gum style --bold "$CHOSENUSERNAME")" \
    "1. Add user to a group" \
    "2. Remove user from a group" \
    "3. Change user's password" \
    "4. Change user's shell" \
    "5. Set new home directory" \
    )"

    OPERATIONCHOICE="$(echo "$USERCHOICE" | awk -F "." '{print $1}')"

    if [[ $OPERATIONCHOICE == "1" ]]; then
        addGroupToUser "$CHOSENUSERNAME"
    elif [[ $OPERATIONCHOICE == "2" ]]; then
        removeGroupFromUser "$CHOSENUSERNAME"
    elif [[ $OPERATIONCHOICE == "3" ]]; then
        sudo passwd "$CHOSENUSERNAME"
        echo "Changed password for user $CHOSENUSERNAME"
    elif [[ $OPERATIONCHOICE == "4" ]]; then
        changeUserShell "$CHOSENUSERNAME"
    elif [[ $OPERATIONCHOICE == "5" ]]; then
        changeUserHomeDirectory "$CHOSENUSERNAME"
    fi
}

# list users, add all selected to specified group
# $1 = group name
addUsersToGroup(){
    USERNAMECHOICE="$(sudo cat /etc/passwd\
    | awk -F ":" '{print $1}'\
    | gum choose --height=8 --no-limit)"
    for i in $USERNAMECHOICE; do
        sudo usermod -aG "$1" "$i"
        echo "Added user $i to group $1"
    done
}

# list users in a group, remove all selected from the group
# $1 = group name
removeUsersFromGroup(){
    # list of the users in the group
    USERLIST=""
    GROUPTABLE="$(sudo cat /etc/group)"
    for i in $GROUPTABLE; do
        if [[ "$(echo "$i" | awk -F ":" '{print $1}')" == "$1" ]]; then
            # tr changes the commas to spaces, so gum choose can read the user list
            USERLIST="$(echo "$i" | awk -F ":" '{print $4}' | tr "," " ")"
            break
        fi
    done
    CHOSENUSERS="$(gum choose --no-limit --height=8 "$USERLIST")"
    for i in $CHOSENUSERS; do
        sudo usermod -rG "$1" "$i"
        echo "Removed user $i from group $1"
    done
}

# function for editing the groups, called from main menu
# < no parameters >
editGroups(){
    # render group list table, hold the chosen line in GROUPTABLECHOICE
    # don't touch the separator, its & because it cant be space or ,
    GROUPTABLECHOICE="$(sudo cat /etc/group \
    | column -s ":" -t -N "Group Name,Password,GID,Users" \
    | gum table --separator="&" --height=8 --widths=120)"

    #filter the chosen line to be just the group name
    CHOSENGROUPNAME="$(echo "$GROUPTABLECHOICE"\
    | awk '{print $1}'\
    | tr -d ' ')"

    if [[ $CHOSENGROUPNAME == "" ]]; then
        echo "No group was specified"
        return
    fi

    #choice of what action to do for the chosen group
    ACTIONCHOICE="$(gum choose \
    --header="Editing group: $(gum style --bold "$CHOSENGROUPNAME")" \
    "1. Add a user(s)" \
    "2. Remove a user(s)" \
    | awk -F "." '{print $1}')"

    if [[ $ACTIONCHOICE == "1" ]]; then
        addUsersToGroup "$CHOSENGROUPNAME"
    elif [[ $ACTIONCHOICE == "2" ]]; then
        removeUsersFromGroup "$CHOSENGROUPNAME"
    fi
}

# function for adding a user, called from main menu
# < no parameters >
addUser(){
    CHOSENUSERNAME=$(gum input --header="Enter the new user's name:" \
    --header.foreground="255")

    if [[ $CHOSENUSERNAME == "" ]]; then
        echo "No user was specified"
        return
    fi

    sudo useradd "$CHOSENUSERNAME"
    echo "Added user $CHOSENUSERNAME"
}

# function for deleting a user, called from main menu
# < no parameters >
deleteUser(){
    CHOSENUSERNAME=$(sudo cat /etc/passwd \
    | awk -F ":" '{print $1}' \
    | gum choose --height=8)

    if [[ $CHOSENUSERNAME == "" ]]; then
        echo "No user was specified"
        return
    fi

    sudo userdel "$CHOSENUSERNAME"
    echo "Removed user $CHOSENUSERNAME"
}

# function for adding a group, called from main menu
# < no parameters >
addGroup(){
    CHOSENGROUPNAME=$(gum input --header="Enter the new group's name:" \
    --header.foreground="255")

    if [[ $CHOSENGROUPNAME == "" ]]; then
        echo "No group was specified"
        return
    fi

    sudo groupadd "$CHOSENGROUPNAME"
    echo "Added group $CHOSENGROUPNAME"
}

# function for removing a group, called from main menu
# < no parameters >
deleteGroup(){
    CHOSENGROUPNAME="$(sudo cat /etc/group \
    | awk -F ":" '{print $1}' \
    | gum choose --height=8)"

    if [[ $CHOSENGROUPNAME == "" ]]; then
        echo "No group was specified"
        return
    fi

    sudo groupdel "$CHOSENGROUPNAME"
    echo "Removed group $CHOSENGROUPNAME"
}

# changes passwords for all users selected to a specified inputted password
# < no parameters >
massChangePasswords(){
    USERNAMECHOICE="$(sudo cat /etc/passwd\
    | awk -F ":" '{print $1}'\
    | gum choose --height=8 --no-limit)"

    if [[ "$USERNAMECHOICE" == "" ]]; then
        echo "No user(s) was selected"
        return
    fi

    PASSWORDCHOICE="$(gum input --header="Type the new password:" \
    --header.foreground="255" --password \
    )"

    PASSWORDCHOICE2="$(gum input --header="Retype the new password:" \
    --header.foreground="255" --password \
    )"

    if [[ "$PASSWORDCHOICE" != "$PASSWORDCHOICE2" ]]; then
        echo "Passwords were not the same"
        return
    fi

    for i in $USERNAMECHOICE; do
        sudo usermod -p "$PASSWORDCHOICE" "$i"
        echo "Changed user $i's password"
    done
}

mainMenu(){
    OPERATIONCHOICE="$(gum choose \
    --header="What action do you want to perform?" \
    "1. Edit a user" \
    "2. Edit a group" \
    "3. Add a user" \
    "4. Delete a user" \
    "5. Add a group" \
    "6. Delete a group" \
    "7. Perform a Mass Password Change" \
    | awk '{print $1}' \
    )"

    # if-structure for choosing options
    if [[ "$OPERATIONCHOICE" == "1." ]]; then
        editUsers
    elif [[ "$OPERATIONCHOICE" == "2." ]]; then
        editGroups
    elif [[ "$OPERATIONCHOICE" == "3." ]]; then
        addUser
    elif [[ "$OPERATIONCHOICE" == "4." ]]; then
        deleteUser
    elif [[ "$OPERATIONCHOICE" == "5." ]]; then
        addGroup
    elif [[ "$OPERATIONCHOICE" == "6." ]]; then
        deleteGroup
    elif [[ "$OPERATIONCHOICE" == "7." ]]; then
        massChangePasswords
    fi
}

# runs everything
mainMenu
