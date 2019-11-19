class Home(View)
    def get(self, request) :
        return render(request, 'main/index.html', {"one" : request.session.get("count", "not found")})
    def post(self, request) :
        name = request.POST.get("name", "no one")
        count = request.session.get("count", 0)
        count = count + 1
        return render(request, 'main/index.html', {"count":count})