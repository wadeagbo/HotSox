from django.shortcuts import render, redirect
from django.urls import reverse
from app_users.models import User, UserMatch, MessageChat
from django.db.models import Q

# Create your views here.


def chat_with_match(request, matched_user_name):
    """Main view to initiate a new chat conversation
    Gather the User, matched user, and all the chats that have been done
    get a chatroom UUID
    """
    error_url = reverse("app_users:user-matches")

    # get the other user object from the unique name
    try:

        matched_user = User.objects.get(username=matched_user_name)
    except User.DoesNotExist:
        # if no valid matched user was found we redirect to error url
        return redirect(error_url)

    # get the UserMatch object to obtain the chatroom UUID
    try:
        user_match_object = UserMatch.objects.get(user=request.user, other=matched_user)
        chatroom_uuid = str(user_match_object.chatroom_uuid)
        request.session["chatroom_uuid"] = chatroom_uuid
    except UserMatch.DoesNotExist:
        # if no valid match was found we redirect to error url
        return redirect(error_url)

    # get all chats send my the current user (to matched user)
    all_chats = MessageChat.objects.filter(
        Q(user=request.user, other=matched_user)
        | Q(user=matched_user, other=request.user)
    ).order_by("sent_date")

    # TODO: implement a message_seen logic ...
    # iterate over the qs all_chats
    # check if "user other == matched_user"
    # check if seen_date is NONE and set to datetime.today()

    context = {
        "sending_user": request.user,
        "receiving_user": matched_user,
        "all_chats": all_chats,
        "chatroom_UUID": chatroom_uuid,
    }

    return render(request, "chat/chat_lobby.html", context)
