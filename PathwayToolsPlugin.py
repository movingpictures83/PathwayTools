import sys
import pythoncyc
import pythoncyc.config as config
from pythoncyc.PToolsFrame import PFrame
#this creates PGDB object associated with meta(MetaCyc)
meta = pythoncyc.select_organism('meta')

class PathwayToolsPlugin:
   def input(self, inputfile):
      params = open(inputfile, 'r')
      self.parameters = dict()
      for line in params:
         contents = line.strip().split('\t')
         self.parameters[contents[0]] = contents[1]
      config.set_host_name(self.parameters['hostname'])
      self.datatype = self.parameters['datatype']

   def run(self):
      pass

   def output(self, outputfile):
      outfile = open(outputfile, 'w')
      if (self.datatype == "pathway"):
         outfile.write(str(pythoncyc.all_orgids())+"\n")
         outfile.write( "*************************************************************************************************************************************************************************************************\n")
         outfile.write( "\n")
         outfile.write( "Pathways:\n")
         for pathway in meta.all_pathways():#meta.pathways_of_compound(sys.argv[1]):
            x = PFrame(pathway, meta, getFrameData=True).__dict__
            outfile.write( "*********************************************************************************************\n")
            outfile.write( "PATHWAY: "+str(x['common_name'].replace("<i>","").replace("</i>","").replace("<b>","").replace("</b>","")))
            outfile.write("\n")
            if 'comment' in x:
               outfile.write( "COMMENT: "+str(x['comment'][0].replace("<i>","").replace("</i>","").replace("<b>","").replace("</b>","").encode('utf-8')))
               outfile.write("\n")
            outfile.write( "INVOLVES: ",)
            for compound in meta.compounds_of_pathway(x['frameid']):
               outfile.write( compound+"\t",) 
            outfile.write( "\nOBSERVED IN: \n")
            count = 1
            if ('species' in PFrame(pathway, meta, getFrameData=True).__dict__):
             for species in PFrame(pathway, meta, getFrameData=True).__dict__['species']:
               outfile.write( str(count)+"."+str(PFrame(species, meta, getFrameData=True).__dict__['names']))
               outfile.write("\n")
               count += 1
            outfile.write( "*********************************************************************************************\n")
      else:
         for pathway in meta.all_pathways():
            if ('species' in PFrame(pathway, meta, getFrameData=True).__dict__):
               for species in PFrame(pathway, meta, getFrameData=True).__dict__['species']:
                  outfile.write(str(PFrame(species, meta, getFrameData=True).__dict__['names']))
                  outfile.write("\n")
