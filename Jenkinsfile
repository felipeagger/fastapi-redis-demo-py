node {
    checkout scm

    // Pega o commit id para ser usado de tag (versionamento) na imagem
    sh "git rev-parse --short HEAD > commit-id"
    tagv = readFile('commit-id').replace("\n", "").replace("\r", "")
    
    // configura o nome da aplicação, o endereço do repositório e o nome da imagem 
    //com a versão
    appName = "fast-api-redis"
    registryHost = "felipeagger/"
    tag = "latest"
    imageName = "${registryHost}${appName}:${tag}"
    
    // Configuramos os estágios
    
    stage "Build"
        def customImage = docker.build("${imageName}")
    //stage "Push"
    //    customImage.push() 
    stage "Deploy PROD"
        input "Deploy to PROD?"
        customImage.push('latest')
        sh "kubectl apply -f https://raw.githubusercontent.com/felipeagger/fastapi-redis-demo-py/master/fastapi-deployment.yaml"
        sh "kubectl set image deployment fast-api-redis app=${imageName} --record"
        sh "kubectl rollout status deployment/fast-api-redis"
}
