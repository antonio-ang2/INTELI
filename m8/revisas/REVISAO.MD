# REVISÃO PROGRAMAÇÃO:

# COESÃO

Coesão refere-se à medida em que as responsabilidades de um módulo ou classe são estreitamente relacionadas. Uma classe coesa faz "uma coisa e faz bem". Quando a coesão é alta, o módulo ou a classe tem um propósito bem definido, o que torna o software mais compreensível, fácil de manter e menos propenso a erros.

# ACOPLAMENTO

Acoplamento refere-se ao grau em que um módulo ou classe depende de outros módulos ou classes. O objetivo é ter o menor acoplamento possível, ou seja, cada módulo ou classe deve operar de forma tão independente quanto possível. Um baixo acoplamento facilita a manutenção, o teste e a reutilização do código.

## Inversão de depedência

A Inversão de Dependência é um dos cinco princípios SOLID do design orientado a objetos, e refere-se a uma forma específica de reduzir o acoplamento

entre módulos ou classes de um software. A ideia principal é que módulos de alto nível, que fornecem funcionalidades complexas, não devem depender de módulos de baixo nível, que fornecem operações detalhadas. Em vez disso, ambos devem depender de abstrações.

Para implementar a inversão de dependência, geralmente seguimos dois princípios fundamentais:

Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações.
Abstrações não devem depender de detalhes. Detalhes devem depender de abstrações.
Isso é frequentemente alcançado através do uso de interfaces (em linguagens que suportam) ou classes abstratas.



# Desing Patterns em Python

A utilização de design patterns é essencial para promover o baixo acoplamento e a alta coesão em sistemas de software. Padrões como Singleton, Factory, Strategy e Dependency Injection são técnicas que incentivam a separação de responsabilidades e a dependência em interfaces ou abstrações, permitindo que componentes interajam sem depender diretamente uns dos outros. Isso leva à redução do acoplamento. Por outro lado, padrões como Composite, Observer e Command incentivam a criação de componentes com funções bem definidas e limitadas, reforçando a coesão. Ao adotar esses padrões, os desenvolvedores podem construir sistemas mais modulares, escaláveis e fáceis de manter.  


## Strategy Pattern

O Strategy Pattern é um padrão de projeto que permite que você defina uma família de algoritmos, encapsule cada um deles e os torne intercambiáveis. Isso significa que você pode alterar o comportamento de uma classe sem alterar seu código, apenas trocando a "estratégia" ou algoritmo que ela usa.

A Inversão de Dependência é um princípio da programação orientada a objetos que sugere que módulos de alto nível não devem depender de módulos de baixo nível, mas ambos devem depender de abstrações. Em outras palavras, em vez de depender de detalhes concretos, seu código deve depender de interfaces ou classes abstratas.

```
strategy

class S3Strategy():
    def upload(self, file):
        # código para upload no S3
        print("Uploading to S3...")

class GCPStrategy():
    def upload(self, file):
        # código para upload no GCP
        print("Uploading to GCP...")

class CloudUploader:
    def __init__(self, service):
        self.service = service

    def upload(self, file):
        if self.service == "S3":
            S3Strategy().upload(file)
        elif self.service == "GCP":
            GCPStrategy().upload(file) ```

```


```
strategy + inversão
from abc import ABC, abstractmethod

class CloudStrategy(ABC):
    @abstractmethod
    def upload(self, file):
        pass

class S3Strategy(CloudStrategy):
    def upload(self, file):
        # código para upload no S3
        print("Uploading to S3...")

class GCPStrategy(CloudStrategy):
    def upload(self, file):
        # código para upload no GCP
        print("Uploading to GCP...")

class CloudUploader:
    def __init__(self, strategy: CloudStrategy):
        self.strategy = strategy

    def upload(self, file):
        self.strategy.upload(file)
 ```


 ## OBSERVER PATTERN

 O Observer Pattern é um padrão de projeto que define uma dependência entre objetos, de modo que quando um objeto muda de estado, todos os seus dependentes são automaticamente notificados e atualizados. É amplamente usado em sistemas que requerem que um componente mantenha outros componentes informados sobre mudanças.

 Coesão: O uso do Observer Pattern aumenta a coesão, já que as responsabilidades estão mais claramente definidas. No exemplo, a lógica de notificação é claramente separada da lógica de publicação.

Acoplamento: O padrão reduz o acoplamento, pois a classe Blog agora não precisa saber os detalhes de como notificar cada assinante. Ela apenas comunica que um evento ocorreu, e é responsabilidade de cada observador decidir como responder.

O Robot Operating System (ROS) utiliza uma variante do Observer Pattern em sua infraestrutura de comunicação. Em ROS, os "publishers" publicam mensagens em tópicos, e os "subscribers" se inscrevem nesses tópicos para receber as mensagens. A relação entre publishers e subscribers em ROS é semelhante à relação entre observáveis e observadores no Observer Pattern.

Vamos ver um exemplo simplificado de como isso funcionaria em um cenário hipotético, onde um subscriber força sua adição a um publisher quando se inscreve em um tópico:



# REQUISITOS DE SOFTWARE

Requisitos funcionais são especificações detalhadas que descrevem as funções, características e interações que um sistema ou software deve possuir. Eles definem o que o sistema deve fazer em resposta a entradas específicas ou em condições determinadas. Em outras palavras, os requisitos funcionais descrevem as funcionalidades que o sistema deve oferecer para atender às necessidades e expectativas dos usuários e dos stakeholders.

## FUNCIONAIS

1.1. Como Definir Requisitos Funcionais
Entendimento do Negócio: Antes de tudo, é crucial entender o domínio do negócio e os objetivos do projeto. Isso fornece um contexto para a definição dos requisitos.

Reuniões e Workshops: Organize sessões de brainstorming com stakeholders, incluindo gerentes de projeto, desenvolvedores, designers e, claro, representantes dos usuários finais.

Use Casos e Histórias de Usuários: Descreva cenários específicos de como os usuários interagirão com o sistema. Isso ajuda a visualizar as funcionalidades necessárias e a identificar possíveis lacunas.

Prototipagem: Crie protótipos ou mockups do sistema para visualizar como ele funcionará. Isso pode ajudar a identificar requisitos adicionais e a obter feedback antecipado.


O cliente, seja ele um usuário final ou um representante de uma organização cliente, é fundamental na definição de requisitos funcionais. Aqui estão as razões:

Perspectiva do Usuário: O cliente oferece uma perspectiva única, a do usuário. Eles podem fornecer insights sobre o que realmente precisam e esperam do sistema.

Validação: Ao envolver o cliente no processo de definição, é possível validar os requisitos à medida que são desenvolvidos, garantindo que o sistema atenda às suas necessidades.

Priorização: O cliente pode ajudar a priorizar requisitos com base em sua importância e valor para o negócio.

Redução de Riscos: Ao entender e documentar corretamente os requisitos do cliente desde o início, reduz-se o risco de retrabalho, custos adicionais e insatisfação do cliente no final do projeto.

Relacionamento e Confiança: Envolver o cliente no processo fortalece o relacionamento e constrói confiança, pois eles veem que suas opiniões e necessidades são valorizadas.


## NÃO FUNCIONAIS

um software também tem requisitos que não estão diretamente relacionados à sua função principal, mas são essenciais para atender às necessidades do usuário final.

Definição: Os requisitos não funcionais descrevem as capacidades operacionais do sistema e tentam melhorar sua funcionalidade. Eles abordam aspectos como velocidade, segurança, confiabilidade e integridade dos dados.

Diferença com Requisitos Funcionais: Enquanto os requisitos funcionais definem o que um produto deve fazer (por exemplo, um mensageiro deve permitir a edição de mensagens), os requisitos não funcionais especificam os atributos de qualidade do sistema.

Tipos de Requisitos Não Funcionais:

- Performance e Escalabilidade: Refere-se à rapidez com que o sistema retorna resultados e como essa performance muda com cargas de trabalho maiores.
- Portabilidade e Compatibilidade: Aborda em quais hardwares, sistemas operacionais e navegadores o software funciona e se ele é compatível com outras aplicações.
- Confiabilidade, Manutenibilidade e Disponibilidade: Estes tratam da frequência de falhas críticas, o tempo necessário para corrigir problemas e a probabilidade de o sistema estar acessível a qualquer momento.
- Segurança: Garante que todos os dados dentro do sistema sejam protegidos contra ataques maliciosos ou acesso não autorizado.
- Localização: Define quão bem um sistema se alinha com o contexto do mercado local, incluindo idiomas, leis, moedas, entre outros.
- Usabilidade: Aborda a facilidade de uso do produto.

Recomendações Gerais:

- Tornar os RNFs mensuráveis e testáveis.
- Definir requisitos para componentes do sistema e não apenas para produtos inteiros.
- Vincular RNFs a objetivos de negócios.
- Considerar limitações de terceiros e arquitetônicas.
- Consultar padrões e guias existentes.

# ENTENDENDO NÓS E TÓPICOS

O sistema ROS 2 (Robot Operating System) é composto por uma série de conceitos fundamentais que, juntos, formam a estrutura de grafo do ROS (2). Este grafo é uma rede de elementos ROS 2 que processam dados simultaneamente. Se fossemos visualizar este grafo, ele englobaria todos os executáveis e as conexões entre eles.

# NÓS

Um "nó" é um dos principais elementos do ROS 2. Cada nó deve ser responsável por uma única função modular. Por exemplo, um nó pode ser responsável por controlar os motores das rodas ou por publicar dados de sensores, como um laser range-finder. Os nós podem enviar e receber dados de outros nós através de tópicos, serviços, ações ou parâmetros. Um sistema robótico completo é composto por muitos nós trabalhando em conjunto. Em ROS 2, um único executável (programa C++, programa Python, etc.) pode conter um ou mais nós.

O ROS 2 utiliza tópicos como um dos principais meios de comunicação entre nós. Os tópicos permitem que os dados sejam transmitidos entre nós, possibilitando a interação e a execução de tarefas complexas em sistemas robóticos. Aqui está um guia sobre como os tópicos funcionam no ROS 2, com base no tutorial fornecido.

# QUATERNIONS



# SERVIÇOS E AÇÕES

Os serviços no ROS 2 são uma forma essencial de comunicação entre os nós. Diferentemente dos tópicos, que operam no modelo de publicação-subscrição, os serviços funcionam com base em um modelo de chamada e resposta. Isso significa que, enquanto os tópicos permitem que os nós se inscrevam em fluxos de dados e recebam atualizações contínuas, os serviços fornecem dados apenas quando são especificamente chamados por um cliente. Aqui está um guia sobre como os serviços funcionam no ROS 2:

Ações no ROS 2 são um tipo de comunicação destinado a tarefas de longa duração. Elas são compostas por três partes: um objetivo (goal), feedback e um resultado (result). As ações são construídas sobre tópicos e serviços, oferecendo funcionalidades semelhantes aos serviços, mas com a capacidade de serem canceladas e fornecerem feedback contínuo.

# NAV2

O nav2, também conhecido como Navigation2, é a segunda geração do sistema de navegação para robôs desenvolvido para funcionar com o ROS 2. É um framework modular e adaptável que fornece todas as ferramentas necessárias para desenvolver e executar algoritmos de navegação em robôs, especialmente robôs móveis. Graças à sua integração com ROS 2, o nav2 aproveita comunicações em tempo real, segurança e outras melhorias essenciais para aplicações robóticas modernas. Sua arquitetura é totalmente baseada em nós, serviços e ações, tendo como uma de suas principais características o uso de árvores de comportamento (behavior trees), que facilitam a definição de comportamento de navegação do robô através de serviços modulares.


# EXPRESSÕES REGULARES

Expressões regulares são sequências de caracteres que formam um padrão de busca. Elas são utilizadas para realizar operações de busca e substituição em textos, bem como para validação de formatos de dados. O poder das expressões regulares reside em sua capacidade de descrever padrões complexos de forma concisa.

A sintaxe das expressões regulares pode parecer intimidadora no início, mas com prática e compreensão dos seus componentes básicos, ela se torna uma ferramenta poderosa. Aqui estão alguns dos elementos fundamentais:

Caracteres Literais: Correspondem exatamente ao caractere especificado. Por exemplo, a regex a corresponderá à letra "a".
Metacaracteres: São caracteres especiais que têm um significado especial. Alguns exemplos incluem . (ponto) que corresponde a qualquer caractere, exceto quebra de linha, e * (asterisco) que indica zero ou mais ocorrências do caractere anterior.
Conjuntos de Caracteres: Delimitados por colchetes [], permitem definir um conjunto de caracteres que podem corresponder. Por exemplo, [abc] corresponderá a "a", "b" ou "c".
Quantificadores: Especificam quantas vezes um caractere ou grupo de caracteres deve aparecer. Alguns exemplos são + (um ou mais), ? (zero ou um) e {n} (exatamente n vezes).
Ancoragem: ^ e $ são utilizados para indicar o início e o fim de uma linha, respectivamente.
Grupos e Captura: Delimitados por parênteses (), permitem agrupar expressões e capturar o texto correspondido para uso posterior.




# Design 

Design inclusivo é diferente de design universal




