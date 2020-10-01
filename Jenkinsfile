node(){
    checkout scm
    sh "ls"

    stage("Build"){
        sh """
        cd workers
        docker build -t 208996231/company:workers .

        cd ..
        cd orders
        docker build -t 208996231/company:orders .

        docker login --username 208996231 --password Huck1212!

        docker push 208996231/company:workers
        docker push 208996231/company:orders
        """
    }

    stage("Test"){
        sh """
        docker login --username 208996231 --password Huck1212!
        docker pull 208996231/company:orders
        docker pull 208996231/company:workers

        docker-compose up -d

        cd tests
        pip3 install requests

        test=\$(python3 workerstest.py http://localhost:9092)

        if [ \$test = "True" ]; then
            echo "Success"
            docker-compose down
        else
            echo "Failed!!"
            docker-compose down
            exit 1
        fi
        """
    }

    stage("Deploy"){
        echo "This is the deployment!!!"
    }

}