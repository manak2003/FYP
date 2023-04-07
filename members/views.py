from django.shortcuts import render
from django.views.generic import ListView
from members.models import UserMembership, Membership, Subscription

# Create your views here.

class MembershipSelectView(ListView):
    model = Membership
    template_name = 'members/membership_list.html'
    context_object_name = 'memberships'
    
    def get_user_membership(self):
        user_membership_qs = UserMembership.objects.filter(user=self.request.user)
        if user_membership_qs.exists():
            return user_membership_qs.first()
        return None
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user_membership = self.get_user_membership(self.request)
        current_user_subscription = self.get_user_subscription(self.request)
        context['current_user_membership'] = str(current_user_membership.membership)
        context['current_user_subscription'] = str(current_user_subscription.active)
        return context


