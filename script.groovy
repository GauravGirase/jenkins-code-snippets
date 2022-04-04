// String filename = 'JenkinsJobs.csv'
// String outputFile = 'output.csv'

// File myfile = new File(filename)
// myfile.readLines().each {
//     def attribute = it.split(',')     // list of attribute
//     // check console output here
//     def status = 'Success'
//     File myfile2 = new File(outputFile)

//     if (myfile2.readLines().size() > 0){


//         myfile2.readLines().each{ b ->

//         println b.split(',')[0] 
//         println attribute[0] 
//         if (b.split(',')[0] == attribute[0]) {
//             println 'Migration is done Already'
//             return
//         }else {
//             println "else block"
            // String  row = it + ',' + status + '\n'
            // myfile2.append(row)
//         }
//     }

//     }else{
//         println "Executed becoz csv is null"
//         String  row = it + ',' + status + '\n'
//         myfile2.append(row)
//     }
    
// }


String filename = 'JenkinsJobs.csv'
String outputFile = 'output.csv'

File myfile = new File(filename)

for(it in myfile.readLines()){
    def attribute = it.split(',')     // list of attribute
    // check console output here
    def status = 'Success'
    File myfile2 = new File(outputFile)

    if (myfile2.readLines().size() > 0){

        boolean found = false;
        for(b in myfile2.readLines()){

        println "parent: " + attribute[0] + " ==? " + b.split(',')[0]
        if (b.split(',')[0] == attribute[0]) {
            println 'Migration is done Already'
            found = true
            println "I am going to break"
            break
        }
        // println "parent: " + attribute[0] + " ==? " + b.split(',')[0]
        

    }
        println "after break"
        if (!found){
            String  row = it + ',' + status + '\n'
            myfile2.append(row)
        }

    }else{
        println "Executed becoz csv is null"
        String  row = it + ',' + status + "\n"
        myfile2.append(row)
    }
    
}

