'''제목: 온프레미스 그리고 클라우드 
'''태그: 클라우드, cloudComputing, cs, 컴퓨터과학
'''시리즈: 클라우드



# 온프레미스와 클라우드

- [온프레미스와 클라우드](#온프레미스와-클라우드)
  - [온프레미스 시스템 구성 및 구축 과정](#온프레미스-시스템-구성-및-구축-과정)
    - [온프레미스 (On-Premise)](#온프레미스-on-premise)
    - [온프레미스 환경에서의 다양한 서버의 종류와 기능](#온프레미스-환경에서의-다양한-서버의-종류와-기능)
    - [온프레미스 시스템의 구성](#온프레미스-시스템의-구성)
    - [온프레미스 시스템 구축 단계](#온프레미스-시스템-구축-단계)
    - [온프레미스 시스템 구축 및 운영 비용](#온프레미스-시스템-구축-및-운영-비용)
    - [개인의 온프레미스 시스템 구축 예](#개인의-온프레미스-시스템-구축-예)
    - [IT 리소스 요구량](#it-리소스-요구량)
    - [IT리소스의 요구량 대비 제공된 처리량](#it리소스의-요구량-대비-제공된-처리량)
    - [유동적 요구량에 따른 리소스 유휴 상태](#유동적-요구량에-따른-리소스-유휴-상태)
  - [클라우드 기반 시스템 구축](#클라우드-기반-시스템-구축)
    - [온프레미스와 클라우드 시스템 구축단계 비교](#온프레미스와-클라우드-시스템-구축단계-비교)
    - [SLA(Service Level Agreement)](#slaservice-level-agreement)
    - [온프레미스와 클라우드 시스템 비용 비교](#온프레미스와-클라우드-시스템-비용-비교)
  - [클라우드 컴퓨팅 이용 방식](#클라우드-컴퓨팅-이용-방식)
    - [클라우드 컴퓨팅 서비스 모델](#클라우드-컴퓨팅-서비스-모델)
    - [클라우드 시스템 배포 모델](#클라우드-시스템-배포-모델)



## 온프레미스 시스템 구성 및 구축 과정
  
### 온프레미스 (On-Premise)
- IT 서비스 제공에 요구되는 데이터 센터에 H/W 및 S/W설비를 자체적으로 보유하고 운용하는 방식
- 클라우드 컴퓨팅 기술이 나오기 전까지 기업의 인프라 구축의 일반적인 방식
- ***개인 혹은 기업이*** IT 서비스를 제공하기 위하여 서버구축
- 이메일, 인터넷 예약, 온라인 쇼핑, 미디어 스트리밍 등 다양한 서비스에 응용

### 온프레미스 환경에서의 다양한 서버의 종류와 기능
- 애플리케이션 서버,HTTP서버, 데이터베이스서버, 메일서버, DNS서버,그룹웨어 서버, 네트워크 관련 서버, 인증 서버

### 온프레미스 시스템의 구성
- 기업이나 개인이 데이터센터를 만들어 고객들에게 서비스를 제공하는 것, 
- 데이터센터와 개발,운용인력이 한 기업조직안에 같은 조직에 있을 떄 온프레미스 시스템이라고 말함

### 온프레미스 시스템 구축 단계
  1. 요구 기능 수집
     1. 사용자의 요청이 무엇인지, 어느정도의 리소스가 필요한지 등
  2. 설계
     1. 서비스를 제공하기 위한, H/W 설계( 용량, 성능 등)
     2. 추가 리소스를 어떻게 확보할 수 있는지 등
  3. 조달
     1. 벤더(vendor)사 선정 및 의뢰, 협상(공급 방법, 가격 등)
     2. 장치별로 벤더사를 선별해야함
     3. 발주에서 조달까지 2-3주 소요
   
  4. 구축
     1. 기업내의 기술력과 경험을 갖춘 인적 자원 활용
     2. 실제로 조달된 컴퓨팅 리소스를 배치하고 가동시키는 것 까지의 활동
     3. 인력이 필요함
  
  5. 운영
     1. 원할하게 작동하는지, S/W의 추가 개발및 모니터링, H/W의 교체 등등 
     2. 서비스를 제공하는 것, 시설관리, H/W 임대, 유지보수, 회선, 운영 담당자 인건비 등 다양한 요소의 부대비용 발생
   
### 온프레미스 시스템 구축 및 운영 비용
  - 직접비용(Hard Cost)
    - IT장비 또는 장비 도입을 하기 위한 외주 비용
    - 운영체제 및 SW, 하드웨어, 로드 밸러싱 및 방화벽, 백업 및 네트워크 장치, 항온, 항습, 전력, 물리 보안, 물리공간
  - 간접비용(Soft Cost)(기회비용이라고도 함)
    -  직무교육, 장비 관리 인력, HW& SW 유지보수 
  
  온프레미스 시스템의 방법은 서비스 제공을 위한 비용을 감당하기에 어려움이 있을 수 있음. 

### 개인의 온프레미스 시스템 구축 예
  - 사용자 수 예상 
  - 초기 자본으로 하드웨어 구매 
  - 서버 발주, 서비스 개시 

> 만약! 사용자 수가 생각보다 많아진다면?!
- 대기열이 쌓이게 됨
- 이 때 다시 발주, 조달, 서버구축, 등등 시간이 많이 소요됨
- 이 사이에 이탈한 고객은 결과적으로 매출감소로 이어짐
- 서버를 추가적으로 증설했는데, 이용자가 이탈하게 되면, 잉여자원 발생, 유지 보수비 증가
- 손실이 커짐
  
### IT 리소스 요구량
- 기업은 리소스를 최소한으로 잡으려고함 
- 예상요구량을 최대한 작게 잡음으로서 비용을 줄이려고 하게 됨
- 기업은 만족돌가 떨어지는 서비스를 제공하게 됨
- 자원관리 비용을 최소화하고 응답시간을 최소화하려는 노력을 계속 해옴

### IT리소스의 요구량 대비 제공된 처리량
- 결핍: 리소스 제공량이 소비스 요구량에 미달된 상태
  
**결핍은 사용자의 불만족으로 이어질 수 밖에 없음**

- 잉여: 리소스 제공량이 서비스의 요구량을 초과한 상태

**잉여는 기업의 손실로 이어질 수 밖에 없음**

### 유동적 요구량에 따른 리소스 유휴 상태
- 리소스 요구량이 일정한 서비는 문제가 없지만, 서비스가 요구량이 요동적인 경우가 많음, 
- 리소스 자원을 평균에 배치하면, 사용자의 불만족과 잉여 둘다 발생
- 피크타임 사용량에 리소스자원을 맞출경우, 질 좋은 서비스를 제공할 수 있겠지만, 피크타임이 아닐 경우, 리소스 잉여만큼 기업의 손실이다. 


> **IT 리소스 제공량이 요구량에 맞춰서 제공된다면 얼마나 좋을까?** 라는 생각이 클라우드시스템의 출발



## 클라우드 기반 시스템 구축

### 온프레미스와 클라우드 시스템 구축단계 비교
- 온프레미스 환경에서의 시스템 구축
  - 요구기능수집, 설계, 조달, 구축, 운영

- 클라우드 환경에서의 시스템 구축
  - 요구기능수집, 설계 ->조달/구축/운영

설계 후 조달부터 운영까지의 시간이 획기적으로 짧음

### SLA(Service Level Agreement)
- IT 리소스를 대여하는 클라우드 서비스 제공자가 사용자에게 제공하는 서비스의 수준을 정량화 하여 명확하게 제시하고, 미달하는 경우 손해 배상하도록 하는 서비스 품질 보장 계약
- SLA 를 통해서 책임소제 문제를 해결하게 됨(?) 클라우드 제공기업에서 품질 보장


### 온프레미스와 클라우드 시스템 비용 비교
- 온프레미스 
  - IDC 비용
  - 커스터마이징, 구축, 하드웨어,IT인력, 유지보수, 교육(훈련) 비용 등이 언제 발생할지 모름
  - CapEx: 물리적인 인프라에 대한 초기비용지출, 시간이 지남에 따라ㅡㄴ 납입 고지서에 비용을 공제하는 지출  
- 클라우드
  - 월사용료가 비싸보여도, 실제 IDC를 구입하는것보다 훨씬 더 많은 비용이 드러나 있어서 숨어있는 비용이 적음(언제 발생할지 모르는 비용이 적음)
  - OpEx: 운용비용, 현재 서비스 또는 제춤에 대해 균등하게 지출되어 청구되는 비용, 초기 비용 없이 사용하는 서비스 또는 제품에 대한 지불방식





## 클라우드 컴퓨팅 이용 방식 

### 클라우드 컴퓨팅 서비스 모델
- IaaS: 하드웨어를 대체하는 방식, H/W 리소스를 제공
  - Netflix는 자체적인 스트리밍 기술을 AWS클라우드 환경에서 구동

- PaaS: H/W리소스와 OS, S/W 개발을 위한 다양한 도구도 같이 제공
  - 구글 App Engine은 애플리케이션을 빌드하고 배포가 가능한 플랫폼 환경을 제공
  - 모바일 게임의 경우 MsSQL 서버 기반의 데이터베이스를 기반으로 프레이어의 데이터를 관리 
  

- SaaS: H/W 리소스와 OS, S/W 모두 제공 
  - 구글 Apps, Dropbox, Notion등 대중화된 애플리케이션 
  
### [클라우드 시스템 배포 모델](./5.클라우드이용모델.md#nist의-클라우드-배포-모델-분류)
- 퍼블릭 클라우드: 다수의 사용자가 클라우드 제공자가 공급하는 서버 및 저장소와 같은 IT 리소스를 공유하여 사용하는 모델

- 프라이빗 클라우드: 단일 조직이 독점적으로 데이터 센터를 구축하고 독점적으로 사용하는 모델

- 하이브리드 클라우드: 둘 이상의 호환되는 여러 클라우드 제공자의 퍼블릭 클라우드의 인프라와 조직 내 구성된 프라이빗 클라우드 인프라가 결합된 모델

- 커뮤니티 클라우드: 업무와 기능이 유사한 경우 조직들 간의 파트너쉽을 맺고 공동으로 접근하고 사용하는 모델
    - 몇몇조직이 협력해서 사용하는 모델 
