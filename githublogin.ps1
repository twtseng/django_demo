$url = "https://github.com/login/oauth/authorize?client_id="+$env:GithubClientId
$resp = Invoke-RestMethod https://github.com/login/oauth/authorize