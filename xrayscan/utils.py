import json
from pprint import pprint
import requests

#settings = {}

def loadSettings():
    global settings
    settf = open("xrayscan/settings.json")
    settings = json.load(settf)
    if not settings["credentials"] or not settings["credentials"]["uname"] or not settings["credentials"]["upass"]:
        raise("Problem with creds in settings")

portPathMap = {
    "17193":"sd.cloudbb.docker.group",
    "17192":"sd.zain-ksa-cloud.docker.group",
    "17191":"sd.zain-ksa-cloud.docker.staging",
    "17190":"sd.zain-ksa-cloud.docker.dev",
    "17189":"sd.zain-ksa-cloud.docker",
    "17188":"gcr_io.docker.proxy",
    "17187":"sd.cloudbb.docker",
    "17186":"it.kolla-victoria-stable.docker",
    "17185":"sd.cloudbb.docker.staging",
    "17184":"sd.cloudbb.docker.dev",
    "17183":"sd.vivophnx-release.mvn.group",
    "17182":"sd.vivophnx.mvn.group",
    "17181":"sd.vivophnx.docker.group",
    "17180":"sd.vivophnx.docker.snapshots",
    "17179":"sd.vivophnx.docker.staging",
    "17178":"sd.vivophnx.docker",
    "17177":"nc.toms2docker.docker.staging",
    "17176":"cs.msdcl-ll.docker",
    "17175":"cs.msdcl-wdyd.docker",
    "17174":"registry_redhat_io.docker.proxy",
    "17172":"sd.adtl.docker",
    "17171":"sd.adtl.docker.staging",
    "17170":"sd.adtl.docker.dev",
    "17169":"sd.adtl.docker.group",
    "17168":"sd.cns.docker",
    "17167":"sd.tmnl.docker.group",
    "17166":"sd.tmnl.docker",
    "17165":"sd.tmnl.docker.staging",
    "17164":"sd.tmnl.docker.dev",
    "17163":"sd.claro-cloud-bss.docker.group",
    "17162":"sd.claro-cloud-bss.docker",
    "17161":"sd.claro-cloud-bss.docker.staging",
    "17160":"sd.claro-cloud-bss.docker.dev",
    "17154":"registry_access_redhat_com.docker.proxy",
    "17153":"cd.operation.docker.dev",
    "17152":"ghcr_io.docker.proxy",
    "17151":"ams_hub_docker_io.docker.proxy",
    "17150":"pd.cloudops-platform.docker.group",
    "17149":"pd.cloudops-platform.docker",
    "17148":"pd.cloudops-platform.docker.staging",
    "17147":"pd.cloudops-platform.docker.dev",
    "17146":"docker_bintray_io.docker.proxy",
    "17145":"sd.svtstand.docker.dev",
    "17143":"it.network-automation.docker",
    "17142":"pd.pm.docker.group",
    "17141":"pd.pm.docker",
    "17140":"pd.pm.docker.staging",
    "17139":"pd.pm.docker.dev",
    "17138":"nc.thirdparty-promoted.docker.repub",
    "17137":"sd.telus-cloud-bss.docker",
    "17136":"sd.telus-cloud-bss.docker.staging",
    "17135":"sd.telus-cloud-bss.docker.dev",
    "17134":"sd.telus-cloud-bss.docker.group",
    "17132":"sd.shaw.bss.docker.group",
    "17131":"sd.tfnuk.portal",
    "17130":"it.civcs.docker",
    "17129":"it.base-images.docker",
    "17128":"it.base-images.docker.group",
    "17127":"it.base-images.docker.dev",
    "17126":"it.base-images.docker.staging",
    "17125":"quay_io.docker.proxy",
    "17124":"sd.swisscom.docker.sync",
    "17123":"pd.mano-cnf-images.docker.dev",
    "17122":"sd.shaw.bss.oracle.docker",
    "17121":"cdc.trn.docker.group",
    "17120":"cdc.trn.docker.staging",
    "17119":"cdc.trn.docker.dev",
    "17118":"pd.utm.docker.group",
    "17117":"cdc.trn.docker",
    "17115":"k8s_gcr_io.docker.proxy",
    "17114":"nc.remote-thirdparty.docker.group",
    "17113":"pd.billing-rating.docker.group",
    "17112":"pd.billing-rating.docker",
    "17111":"pd.billing-rating.docker.staging",
    "17110":"pd.billing-rating.docker.dev",
    "17109":"dp.jenkins-k8s.docker",
    "17108":"dp.jenkins-k8s.docker.dev",
    "17107":"pd.sandbox-dev.docker.group",
    "17106":"pd.utm.docker",
    "17105":"pd.utm.docker.staging",
    "17104":"pd.utm.docker.dev",
    "17103":"pd.pmwp.docker.group",
    "17102":"sd.rktn_ssp_cloud_poc.docker",
    "17101":"sd.rktn_ssp_cloud_poc.docker.staging",
    "17100":"sd.rktn_ssp_cloud_poc.docker.snapshots",
    "17099":"pd.sandbox-staging.docker.group",
    "17097":"pd.sandbox-release.docker.group",
    "17096":"sd.shaw.bss.docker.dev",
    "17095":"pd.pmwp.docker",
    "17094":"pd.pmwp.docker.staging",
    "17093":"pd.pmwp.docker.dev",
    "17092":"pd.billing.test.docker",
    "17091":"ocs.nextbilling.docker.dev",
    "17090":"nc.thirdparty-internal.docker.repub",
    "17089":"sd.tim.docker",
    "17088":"sd.tim.docker.snapshots",
    "17087":"sd.tim.docker.staging",
    "17086":"sd.amxcpq.docker.group",
    "17085":"sd.nec-vnf-plugin.docker.repub",
    "17084":"pd.jenkins.docker.group",
    "17083":"pd.jenkins.docker",
    "17082":"pd.jenkins.docker.staging",
    "17081":"pd.jenkins.docker.dev",
    "17080":"sd.o2.tfnuk.ntfngn.docker.dev",
    "17079":"pd.cloudops.docker",
    "17078":"sd.amxcpq.docker",
    "17077":"sd.amxcpq.docker.staging",
    "17076":"sd.amxcpq.docker.snapshots",
    "17075":"pd.nb_services.docker",
    "17074":"pd.nb_services.docker.staging",
    "17073":"pd.nb_services.docker.snapshots",
    "17072":"pd.nb_services.mvn",
    "17071":"pd.nb_services.mvn.staging",
    "17070":"pd.nb_services.mvn.snapshots",
    "17069":"pd.gui.docker.dev",
    "17068":"it.monitoring.docker",
    "17067":"cs.msdcl.base.docker.dev",
    "17066":"demo.ocsbaseline.docker.dev",
    "17065":"nc.sandbox-internal.docker",
    "17064":"hub_docker_io.docker.proxy",
    "17063":"sd.shawoss.files.dev",
    "17062":"sd.shaw.bss.build-system.docker",
    "17061":"it.openshift.docker",
    "17060":"it.public_clouds.docker.transfer",
    "17059":"demo.cloud.docker.staging",
    "17058":"demo.cloud.docker.group",
    "17056":"pd.paas-enterprise.docker.repub",
    "17055":"pd.toms-release.npm.group",
    "17054":"dp.pati-recycle-bin.generic",
    "17053":"pd.ocs.docker.dev",
    "17052":"sd.tfgt.docker.dev",
    "17051":"it.uvpn.docker",
    "17050":"demo.cloud.docker.dev",
    "17049":"demo.cloud.docker",
    "17048":"it.cloudsupport.docker",
    "17047":"it.openshiftss.docker.repub",
    "17046":"sd.cogemnrch.docker.staging.r2b2",
    "17045":"sd.cogemnrch.docker.dev.r2b2",
    "17044":"sd.vivols.docker.group",
    "17043":"sd.cogemnrch.docker.staging",
    "17042":"sd.cogemnrch.docker.dev",
    "17041":"sd.vivols.docker",
    "17040":"sd.vivols.docker.staging",
    "17039":"sd.vivols.docker.snapshots",
    "17038":"demo.sdwan.docker.dev",
    "17036":"pd.licensing.docker.dev",
    "17035":"dp.idbp.docker.dev",
    "17034":"docker_netcracker_com-nc-int-builds-release.files.legacy",
    "17033":"nexusnpmcn_netcracker_com-nc-npm-dev.npm.legacy",
    "17032":"docker_netcracker_com-product.docker.legacy",
    "17031":"docker_netcracker_com-nc-product-deploy.mvn.legacy",
    "17029":"ta.atp.docker.dev",
    "17028":"ta.atp.docker",
    "17027":"demo.portals.docker.dev",
    "17026":"pd.hom.docker.dev",
    "17025":"nc_docker_1",
    "17024":"pd.tsdn.docker.dev",
    "17023":"pd.search.docker.dev",
    "17022":"pd.security.docker.dev",
    "17021":"cs.msdcl.docker.dev",
    "17020":"it.kubernetes-kismatic.docker",
    "17019":"it.saas-si-prod.docker.staging",
    "17018":"it.saas-si-prod.docker.release",
    "17017":"it.training.docker",
    "17016":"pd.saas-sfa.docker.dev",
    "17015":"demo.service-modeling.docker",
    "17014":"nc.sandbox.docker",
    "17013":"demo.service-modeling.docker.dev",
    "17012":"pd.saas-dep.docker",
    "17011":"it.dpl.docker.dev",
    "17010":"nc.thirdparty.docker.repub",
    "17009":"nc.sandbox.docker.dev",
    "17008":"nc.sandbox.docker.staging",
    "17007":"demo.cloudmano-vfw-pa.docker.dev",
    "17006":"pd.saas-dep.docker.dev",
    "17004":"pd.saas.docker.group",
    "17003":"pd.saas.docker",
    "17002":"pd.saas.docker.staging",
    "17001":"pd.saas.docker.dev",
}

def resolveImage(image):
    imagePath = image.split("/", 1)
    host = imagePath[0].split(":")
    repo = portPathMap[host[1]]
    # repo = repo.replace("docker.group", "docker")
    imagePath = imagePath[1].replace(":", "/")
    fullPath = repo + "/" + imagePath + "/manifest.json"

    session = requests.Session()
    session.auth = (settings["credentials"]["uname"], settings["credentials"]["upass"])
    url = "https://artifactorycn.netcracker.com/artifactory/api/storage/" + fullPath
    result = session.get(url)
    if result.status_code != 200:
        print("Error getting storage image information for " + fullPath)
        pprint(result.text)
        return "ERROR"
        
    fileInfo = result.json()
    sha2 = fileInfo["checksums"]["sha256"]

    url = "https://artifactorycn.netcracker.com/artifactory/api/search/checksum?sha256=" + sha2
    filePaths = session.get(url).json()
    for u in filePaths["results"]:
        if u["uri"].endswith("manifest.json"):
            return u["uri"].replace("https://artifactorycn.netcracker.com/artifactory/api/storage/", "")

    return ""
    #return filePaths["results"][0]["uri"].replace("https://artifactorycn.netcracker.com/artifactory/api/storage/", "")

def findBySHA2(sha2):
    session = requests.Session()
    session.auth = (settings["credentials"]["uname"], settings["credentials"]["upass"])
    url = "https://artifactorycn.netcracker.com/artifactory/api/search/checksum?sha256=" + sha2
    result = session.get(url)
    filePaths = result.json()
    if result.status_code != 200:
        print(result.text)
        return ""
        
    for u in filePaths["results"]:
        if u["uri"].endswith("manifest.json"):
            return u["uri"].replace("https://artifactorycn.netcracker.com/artifactory/api/storage/", "")

    return ""

def findBaseFrom(docker):
    docker = docker.splitlines()
    for line in docker:
        if not line.startswith("FROM"):
            continue

        line  = line.split(" ")
        if len(line) > 2:
            continue

        return line[1]

    return ""

def getImageStructure(repo, image):
    session = requests.Session()
    session.auth = (settings["credentials"]["uname"], settings["credentials"]["upass"])
    url = "https://artifactorycn.netcracker.com/artifactory/api/storage/" + repo + "/" + image + "?list&deep=1&listFolders=1&mdTimestamps=1"
    print("Listing: " + url)
    files = session.get(url)
    #print(files.text)
    files = files.json()
    if 'errors' in files:
        print("ERROR: Errors while listing:")
        for err in files['errors']:
            print(err['message'])
        return None

    layers = []
    isImage = False
    for file in files['files']:
        if file['uri'] == "/manifest.json":
            isImage = True
            continue

        #print(f"{file['uri']} : {file['sha2']}")
        layers.append(file['sha2'])
    
    if not isImage:
        print("ERROR: Manifest not found! (Not an image?)")
        return None

    imageStructure = {
        "path": repo + "/" + image,
        "layers": layers
    }
    return imageStructure

def searchArtifactByName(name):
    session = requests.Session()
    session.auth = (settings["credentials"]["uname"], settings["credentials"]["upass"])
    session.headers = {"X-Result-Detail":"info"}
    url = "https://artifactorycn.netcracker.com/artifactory/api/search/artifact?name=" + name
    files = session.get(url)
    if files.status_code != 200:
        return None

    return files.json()

loadSettings()